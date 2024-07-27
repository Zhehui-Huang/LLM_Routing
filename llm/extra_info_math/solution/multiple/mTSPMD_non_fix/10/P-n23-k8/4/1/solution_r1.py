import numpy as np
from scipy.spatial.distance import euclidean
import pulp

# List of city coordinates, including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Total number of vehicles
num_robots = 8
# All robots start from depot city 0
start_depot_index = 0

# Distances matrix using Euclidean distance
distances = cdist(coordinates, coordinates, metric='euclidean')

# Setting up the problem
prob = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Variables: x[i][j] is 1 if robot travels from city i to city j
x = [[pulp.LpVariable(f"x_{i}_{j}", cat='Binary') 
      for j in range(len(coordinates))] for i in range(len(coordinates))]

# Objective Function: Minimize total travel cost
prob += pulp.lpSum(distances[i][j] * x[i][j] 
                   for i in range(len(coordinates)) 
                   for j in range(len(coordinates)) if i != j)

# Constraints
# All robots start at the initial depot
prob += pulp.lpSum(x[start_depot_index][j] for j in range(1, len(coordinates))) == num_robots

# Each city must be visited exactly once, ignoring the starting depot
for j in range(1, len(coordinates)):
    prob += pulp.lpSum(x[i][j] for i in range(len(coordinates)) if i != j) == 1

# Leaving from each city (vehicles going to different cities)
for i in range(1, len(coordinates)):
    prob += pulp.lpSum(x[i][j] for j in range(len(coordinates)) if i != j) == 1

# Each vehicle leaving a city arrives at another city (flow conservation for 1 vehicle)
for i in range(1, len(coordinates)):
    prob += (pulp.lpSum(x[k][i] for k in range(len(coordinates)) if k != i) 
            == pulp.lpSum(x[i][j] for j in range(len(coordinates)) if j != i))

# Solve the problem
prob.solve()

# Extracting the solution
routes = [[] for _ in range(num_robots)]
active_vehicles = 0

for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if pulp.value(x[i][j]) == 1:
            print(f"Route from {i} to {j} is selected")
            if i == start_depot_index:
                routes[active_vehicles].append(i)
                routes[active_vehicles].append(j)
                active_vehicles += 1
            else:
                # Find the correct route list and append
                for route in routes:
                    if route[-1] == i:
                        route.append(j)

# Calculating costs per route and total cost
overall_total_cost = 0
for idx, route in enumerate(routes):
    total_cost = sum(distances[route[k]][route[k+1]] for k in range(len(route)-1))
    overall_total_cost += total_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {total_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")