import numpy as np
from scipy.spatial.distance import euclidean
import pulp

# Define the problem parameters
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
num_robots = 8
robot_capacity = 40

# Distance matrix
n = len(coords)
distance_matrix = [[euclidean(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Problem setup
problem = pulp.LpProblem("VRP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j, k) for k in range(num_robots) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
problem += pulp.lpSum(distance_matrix[i][j] * x[i, j, k] for k in range(num_robots) for i in range(n) for j in range(n) if i != j)

# Constraint: Each city is visited exactly once
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for k in range(num_robots) for i in range(n) if i != j) == 1

# Constraint: Satisfy demand within capacity limits
for k in range(num_robots):
    problem += pulp.lpSum(demands[j] * x[i, j, k] for i in range(n) for j in range(1, n) if i != j) <= robot_capacity

# Constraints: Flow conservation
for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1
    for j in range(1, n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

# Solve the problem
problem.solve()

# Check problem status and display routes
if pulp.LpStatus[problem.status] == 'Optimal':
    print("Found an optimal solution.")
    total_distance = 0
    for k in range(num_robots):
        route = []
        for i in range(n):
            for j in range(n):
                if i != j and pulp.value(x[i, j, k]) == 1:
                    route.append((i, j))
        if route:
            print(f"Robot {k} route: {route}")
            route_distance = sum(distance_matrix[i][j] for (i, j) in route)
            total_distance += route,"Cost:", route_distance)
            print("Route Cost:", route_distance)
    print("Overall Total Distance:", total_distance)
else:
    print("No optimal solution found, status:", pulp.LpStatus[problem.status])