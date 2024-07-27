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

# Objective function
model += pulp.lpSum(x[(r, i, j)] * distance(i, j)
                    for r in range(number_of_robots) 
                    for i in range(len(cities)) 
                    for j in range(len(cities)) 
                    if i != j)

# Constraints

# Supply each city exactly once
for j in range(1, len(cities)):
    model += pulp.lpSum(x[(r, i, j)] for r in range(number_of_robots) for i in range(len(cities)) if i != j) == 1

# Depart and return to the depot exactly once per robot
for r in range(number_of_robots):
    model += pulp.lpSum(x[(r, 0, j)] for j in range(1, len(cities))) == 1
    model += pulp.lpSum(x[(r, j, 0)] for j in range(1, len(cities))) == 1

# Load capacity does not exceed limits
for r in range(number_of_robots):
    model += pulp.lpSum(x[(r, i, j)] * demands[j] for i in range(len(cities)) for j in range(1, len(cities)) if i != j) <= robot_capacity

# Solve the model
if model.solve() == pulp.LpStatusOptimal:
    total_cost = 0
    for r in range(number_of_robots):
        tour = [0]
        next_city = 0
        tour_cost = 0
        while True:
            found = False
            for j in range(len(cities)):
                if pulp.value(x[(r, next_city, j)]) == 1:
                    if j == 0:
                        tour_cost += distance(next_city, j)
                        tour.append(j)
                        total_cost += tour_cost
                        print(f"Robot {r} Tour: {tour}")
                        print(f"Robot {r} Total Travel Cost: {tour_cost}")
                        tour_cost = 0
                        tour = [0]
                        break
                    tour.append(j)
                    tour_cost += distance(next_city, j)
                    next_city = j
                    found = True
                    break
            if not found:
                break

    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No optimal solution found.")