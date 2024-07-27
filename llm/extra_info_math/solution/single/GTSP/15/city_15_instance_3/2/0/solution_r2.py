import math
import numpy as np
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary, PULP_CBC_CMD

# City coordinates
cities = {
    0: (16, 90), 
    1: (43, 99), 
    2: (80, 21), 
    3: (86, 92), 
    4: (54, 93), 
    5: (34, 73), 
    6: (6, 61), 
    7: (86, 69), 
    8: (30, 50), 
    9: (35, 73), 
    10: (42, 64), 
    11: (64, 30), 
    12: (70, 95), 
    13: (29, 64), 
    14: (32, 79),
}

# City groups
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create model
model = LpProblem("Minimize_Distance", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", (i for i in range(15)), 0, 1, LpBinary)

# Create a "super source"
super_source_group = [i for i in range(len(groups)) for _ in groups[i]]

# Add multiple robots start and end at the start point, constraint to visit all cities across groups but only one in each group
u = LpVariable.dicts("u", ((i, j) for i in range(15) for j in range(15)), lowBound=0, cat='Continuous')

# Objective: Minimize the travel distance
model += lpSum(u[i, j] * distance(i, j) for i in range(15) for j in range(15) if i != j)

# Constraint: Enter and leave each group exactly once
for group in groups:
    model += lpSum(x[i] for i in group) == 1

# Constraint: Subtour elimination
for i in range(15):
    for j in range(15):
        if i != j:
            model += u[i, j] <= len(cities) * (x[i] + x[j] - 1)
            model += u[i, j] >= x[j] - x[i]

# Flow constraint
for i in range(15):
    model += lpSum(u[i, j] for j in range(15) if i != j) - lpSum(u[j, i] for j in range(15) if i != j) == 0

# Constraint: Same group cannot have two cities selected together
for group in groups:
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            model += x[group[i]] + x[group[j]] <= 1

# Solve the problem
model.solve(PULP_CBC_CMD(msg=0))

# Extract the solution
tour = []
for i in range(15):
    if x[i].varValue == 1:
        tour.append(i)

# Calculate the total distance
total_distance = sum(u[i, j].varValue * distance(i, j) for i in range(15) for j in range(15) if i != j and u[i, j].varValue > 0)

# Output results
print("Tour:", [0] + tour + [0])
print("Total travel cost:", total_distance)