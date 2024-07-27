import numpy as np
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value
from itertools import product

# Coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
               (62, 63), (63, 69), (45, 35)]

# Parameters
n = len(coordinates)  # Total nodes, including the depot
m = 2                 # Number of robots
indices = range(n)
pairs = [(i, j) for i in indices for j in indices if i != j]
range_m = range(m)

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Costs matrix
cost_matrix = {
    (i, j): euclidean_distance(coordinates[i], coordinates[j])
    for i, j in pairs
}


# Problem formulation
prob = LpProblem("MTRP", LpMinimize)
x = LpVariable.dicts('x', (indices, indices, range_m), cat='Binary', lowBound=0, upBound=1)
u = LpVariable.dicts('u', indices[1:], lowBound=0, upBound=n-1, cat='Continuous')


# Objective function
g = LpVariable('g', lowBound=0, cat='Continuous')
prob += g

# Constraints
for j in indices[1:]:
    prob += lpSum(x[i][j][k] for i in indices if i != j for k in range_m) == 1

for i in indices:
    for k in range_m:
        prob += lpSum(x[i][j][k] for j in indices if i != j) == lpSum(x[j][i][k] for j in indices if i != j)
        
for k in range_m:
    prob += lpSum(x[0][j][k] for j in indices if j != 0) == 1

for i, j in pairs:
    if i != j and i != 0 and j != 0:
        for k in range_m:
            prob += u[i] - u[j] + n * x[i][j][k] <= n - 1

for k in range_m:
    prob += lpSum(cost_matrix[i, j] * x[i][j][k] for i, j in pairs) <= g

# Solve the problem
prob.solve()

# Results
print("Status:", LpStatus[prob.status])

for k in range_m:
    print(f"Robot {k} Tour: ", end='')
    for i in indices:
        for j in indices:
            if x[i][j][k].varValue == 1:
                print(f'{i}->{j} ', end='')
    print("\n")

# Maximum travel cost
print(f"Maximum Travel Cost: {value(g)}")