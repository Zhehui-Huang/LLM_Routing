import numpy as np
from pulp import LpMinimize, LpProblem, LpVariable, LpInteger, lpSum, LpBinary

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Compute Euclidean distance matrix
def euclidean_distance(p1, p2):
    return round(np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))

n = len(coordinates)
c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Number of salesmen (robots)
m = 8

# Problem
problem = LpProblem("VRP", LpMinimize)

# Variables
x = [[[LpVariable(f"x_{i}_{j}_{k}", cat=LpBinary) for k in range(m)] for j in range(n)] for i in range(n)]
u = [LpVariable(f"u_{i}", lowBound=0, cat=LpInteger) for i in range(n)]

# Objective
problem += lpSum(c[i][j] * x[i][j][k] for k in range(m) for i in range(n) for j in range(n))

# Each city is visited exactly once by one salesman
for j in range(1, n):  # Skip depot in sums
    problem += lpSum(x[i][j][k] for i in range(n) for k in range(m)) == 1

# Flow conservation constraints
for k in range(m):
    for j in range(1, n):  # Skip depot in sums
        problem += lpSum(x[i][j][k] for i in range(n)) == lpSum(x[j][i][k] for i in range(n))

# Salesman leaves and enters the depot constraints
for k in range(m):
    problem += lpSum(x[0][j][k] for j in range(1, n)) == 1
    problem += lpSum(x[j][0][k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n-1) * x[i][j][k] <= n - 2

# Solve the problem
problem.solve()

# Gather results
tours = [[0] for _ in range(m)]
costs = [0] * m
for k in range(m):
    for i in range(n):
        for j in range(n):
            if x[i][j][k].varValue == 1:
                tours[k].append(j)
                costs[k] += c[i][j]

# Ensure tours start and end at depot
for k in range(m):
    if len(tours[k]) > 1:  # Only append ending depot if tour is non-trivial
        tours[k].append(0)
    else:
        costs[k] = 0  # No cost if robot does not travel

# Display results
total_cost = 0
for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
    total_cost += costs[k]

print(f"Overall Total Travel Top Cost: {total_cost}")