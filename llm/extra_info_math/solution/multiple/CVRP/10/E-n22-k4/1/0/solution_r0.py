import pulp
from math import sqrt

# Data
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
robot_capacity = 6000
number_of_robots = 4

# Calculate Euclidean distance
def distance(city1, city2):
    x_diff = cities[city1][0] - cities[city2][0]
    y_diff = cities[city1][1] - cities[city2][1]
    return sqrt(x_diff**2 + y_diff**2)

# Problem variables
model = pulp.LpProblem("CVRP", pulp.LpMinimize)

x = {}  # binary variable x[robot, from_node, to_node]
for r in range(number_of_robots):
    for i in range(len(cities)):
        for j in range(len(cities)):
            if i != j:
                x[(r, i, j)] = pulp.LpVariable(f"x_{r}_{i}_{j}", 0, 1, pulp.LpBinary)

# Objective function: Minimize distance
model += pulp.lpSum(x[(r, i, j)] * distance(i, j)
                   for r in range(number_of_robots) for i in range(len(cities)) for j in range(len(cities)) if i != j)

# Constraints

# Serve each city exactly once
for j in range(1, len(cities)):
    model += pulp.lpSum(x[(r, i, j)] for r in range(number_of_robots) for i in range(len(cities)) if i != j) == 1

# Each robot leaves and enters depot exactly once
for r in range(number_of_robots):
    model += pulp.lpSum(x[(r, 0, j)] for j in range(1, len(cities))) == 1
    model += pulp.lpSum(x[(r, j, 0)] for j in range(1, len(cities))) == 1

# Load capacity requirements
for r in range(number_of_robots):
    model += pulp.lpSum(x[(r, i, j)] * demands[j] for i in range(len(cities)) for j in range(1, len(cities))) <= robot_capacity

# Flow conservation
for r in range(number_of_robots):
    for j in range(1, len(cities)):
        model += pulp.lpSum(x[(r, i, j)] for i in range(len(cities)) if i != j) == \
                 pulp.lpSum(x[(r, j, k)] for k in range(len(cities)) if j != k)

# Solve the problem
solution_status = model.solve()

# Verify and build output
if solution_status == pulp.LpStatusOptimal:
    for r in range(number_of_robots):
        tour = [0]
        current_city = 0
        while True:
            next_city = None
            for j in range(len(cities)):
                if j != current_city and pulp.value(x[(r, current_city, j)]) == 1:
                    next_city = j
                    tour.append(next_city)
                    current_city = j
                    break
            if next_city == 0:
                break
        travel_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        print(f"Robot {r} Tour: {tour}")
        print(f"Robot {r} Total Travel Cost: {travel_cost}")

    overall_cost = pulp.value(model.objective)
    print(f"Overall Total Travel Cost: {overall_cost}")
else:
    print("No optimal solution was found.")