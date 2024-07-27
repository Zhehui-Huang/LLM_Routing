import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations
import pulp

# Cities coordinates
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Demands by each city
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Number of robots and their capacities
num_robots = 8
robot_capacity = 40

# Distance matrix
n = len(coords)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i, j] = euclidean(coords[i], coords[j])
        else:
            dist_matrix[i, j] = 0

# Solving the problem using pulp for linear problem optimization
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variable, x[i,j,k] = 1 if robot k travels from city i to j
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(num_robots) if i != j), cat='Binary')

# Constraints and objective
problem += pulp.lpSum(dist_matrix[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(num_robots) if i != j)

# Each city needs to be visited exactly once and demands met
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(num_robots) if i != j) == 1

# Departures and arrivals for robots at depot
for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1 # depart from depot
    problem += pulp.lpSum(x[i, 0, k] for i in range(1, n)) == 1 # arrive at depot

# Load constraint per robot
for k in range(num_robots):
    problem += pulp.lpSum(demands[j] * x[i, j, k] for i in range(n) for j in range(1, n) if i != j) <= robot_capacity

# Capacity and travel conservation constraints
for j in range(1, n):
    for k in range(num_robots):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) - pulp.lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# Solve the problem
status = problem.solve(pulp.APISolver(msg=1))
print("Status:", pulp.LpStatus[status])

# Print routes and cost
total_cost = 0
for k in range(num_robots):
    tour = [0]
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[i, j, k]) == 1:
                tour.append(j)
                if j == 0:
                    break
        if tour[-1] == 0:
            break
    cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    total_cost += cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {cost}\n")

print("Overall Total Travel Theoretical Cost:", total_cost)