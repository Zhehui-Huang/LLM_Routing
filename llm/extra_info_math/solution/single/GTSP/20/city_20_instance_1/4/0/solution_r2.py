import pulp
from math import sqrt

# City coordinates, including the depot (city 0)
coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Groups of cities, including the depot (city 0) for each group
groups = [
    [0, 5, 6, 7, 11, 17],
    [0, 1, 4, 8, 13, 16],
    [0, 2, 10, 15, 18, 19],
    [0, 3, 9, 12, 14]
]

# Function to calculate Euclidean distance
def calc_distance(i, j):
    return sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)

# Create the LP problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if path from i to j is chosen, otherwise 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(20) for j in range(20) if i != j), cat='Binary')

# Objective Function: Minimize distance
problem += pulp.lpSum(x[(i, j)] * calc_distance(i, j) for i in range(20) for j in range(20) if i != j)

# Constraint: Enter each group only once
for group in groups:
    problem += pulp.lpSum(x[(i, j)] for i in range(20) for j in group if i != j) == 1

# Constraint: Leave each group only once
for group in groups:
    problem += pulp.lpSum(x[(i, j)] for j in range(20) for i in group if i != j) == 1

# Flow conservation for each city not being a depot
for k in range(1, 20):
    problem += pulp.lpSum(x[(i, k)] for i in range(20) if i != k) - pulp.lpChange