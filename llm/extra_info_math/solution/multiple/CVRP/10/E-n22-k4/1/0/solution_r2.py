import pulp
from math import sqrt

# Data setup
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

# Euclidean distance calculator
def distance(city1, city2):
    x_diff = cities[city1][0] - cities[city2][0]
    y_diff = cities[city1][1] - cities[city2][1]
    return sqrt(x_diff**2 + y_diff**2)

# Optimizer model
model = pulp.LpProblem("CVRP", pulp.LpMinimize)
x = {(r, i, j): pulp.LpVariable(f"x_{r}_{i}_{j}", cat='Binary')
     for r in range(number_of_robots) for i in cities for j in cities if i != j}

# Objective: Minimize total cost across all routes
model += pulp.lpSum(distance(i, j) * x[r, i, j] for r in range(number_of_robots) for i in cities for j in cities if i != j)

# Constraints
# Ensure each city is visited exactly once (excluding depot)
for j in cities:
    if j != 0:
        model += pulp.lpSum(x[r, i, j] for r in range(number_of_robots) for i in cities if i != j) == 1

# Each robot starts and ends at the depot
for r in range(number_of_robots):
    model += pulp.lpSum(x[r, 0, j] for j in cities if j != 0) == 1
    model += pulp.lpSum(x[r, j, 0] for j in cities if j != 0) == 1

# Capacity constraints
for r in range(number_of_robots):
    model += pulp.lpSum(demands[j] * x[r, i, j] for i in cities for j in cities if i != j) <= robot_capacity

# Solve the problem
model.solve()

# Parse and display the results
path_costs = []
for r in range(number_of_robots):
    route = []
    next_location = 0
    while True:
        next_city_found = False
        for j in cities:
            if j != next_location and x[r, next_location, j].varValue == 1:
                route.append(next_location)
                next_location = j
                next_city_found = True
                break
        if not next_city_found or next_location == 0:
            route.append(0)
            break

    route_cost = sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))
    path_costs.append(route_cost)
    print(f"Robot {r} Tour: {route}")
    print(f"Robot {r} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {sum(path_costs):.2f}")