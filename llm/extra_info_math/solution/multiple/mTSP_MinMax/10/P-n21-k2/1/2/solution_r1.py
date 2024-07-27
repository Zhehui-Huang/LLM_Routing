import numpy as np
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, PulpSolverError

coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
               (62, 63), (63, 69), (45, 35)]
n = len(coordinates)  # Number of nodes
m = 2  # Number of salesmen

# Euclidean Distance
def distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost dictionary
costs = {(i, j): distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Variables
x = LpVariable.dicts('x', [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], cat='Binary')
u = LpVariable.dicts('u', list(range(1, n)), lowBound=1, upBound=n-1, cat='Continuous')

problem = LpProblem("mTSP", LpMinimize)

# Objective
problem += lpSum(costs[i, j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j), "Total_Cost"

# Constraints
# Visit each city exactly once (excluding depot)
for j in range(1, n):
    problem += lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1, f"Visit_{j}"

# Salesman leaves and enters starting city exactly once
for k in range(m):
    problem += lpSum(x[0, j, k] for j in range(1, n)) == 1, f"Start_{k}"
    problem += lpSum(x[j, 0, k] for j in range(1, n)) == 1, f"End_{k}"

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1) * lpSum(x[i, j, k] for k in range(m)) <= n - 2, f"Subtour_{i}_{j}"

# Flow conservation
for k in range(m):
    for j in range(1, n):
        problem += lpSum(x[i, j, k] for i in range(n) if i != j) == lpSum(x[j, i, k] for i in range(n) if i != j), f"Flow_{k}_{j}"

# Solve problem
try:
    status = problem.solve()
    print(f"Status: {LpStatus[problem.status]}")

    if LpStatus[problem.status] == 'Optimal':
        paths = {k: [] for k in range(m)}
        for k in range(m):
            tour = [0]
            while True:
                next_cities = [
                    j for j in range(n) 
                    if j not in tour and x[tour[-1], j, k].varValue == 1
                ]
                if not next_cities:
                    break
                tour.append(next_cities[0])
            tour.append(0)  # Add depot at the end
            paths[k] = tour
            print(f"Robot {k} Tour: {paths[k]}")
            tour_cost = sum(costs[paths[k][i], paths[k][i + 1]] for i in range(len(paths[k]) - 1))
            print(f"Robot {k} Total Travel Cost: {tour_cost}")

except PulpSolverError:
    print("Solver failed to find a solution.")