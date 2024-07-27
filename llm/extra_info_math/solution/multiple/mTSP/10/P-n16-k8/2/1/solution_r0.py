import numpy as np
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Define cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots
m = 8
# Total nodes, including the depot
n = len(coordinates)

# Calculating Euclidean distance matrix
def euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Travel cost between every pair of nodes
c = [[euclidean distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem setup
prob = LpProblem("RobotRouting", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat=LpBinary)
u = LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective Function
prob += lpSum(c[i][j] * x[i, j, k] for i in range(1, n) for j in range(1, n) for k in range(m) if i != j)

# Constraints
# Every city is visited exactly once by one robot
for j in range(1, n):
    prob += lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        prob += lpSum(x[i, p, k] for i in range(n) if i != p) - lpSum(x[p, j, k] for j in range(n) if j != p) == 0

# Each salesman must leave the depot exactly once
for k in range(m):
    prob += lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + n * x[i, j, k] <= n - 1