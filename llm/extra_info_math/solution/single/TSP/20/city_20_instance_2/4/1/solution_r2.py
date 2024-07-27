import numpy as np
from pulp import *
import math

# Define the cities coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Number of cities including depot
n = len(cities)

# Create the problem
prob = LpProblem("TSP", LpMinimize)

# Create decision variables
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 0, 1, LpBinary)

# Objective function
prob += lpSum(x[(i, j)] * distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # Leave each city only once
    prob += lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # Enter each city only once

# Subtour elimination constraints
for S in range(2, n):
    for subset in combinations(range(1, n), S):
        prob += lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Output the solution
tour = []
visited = [0]  # Start at depot
while len(visited) < n:
    for j in range(n):
        if x[(visited[-1], j)].varValue == 1:
            visited.append(j)
            break
tour = visited + [0]  # Return to depot

# Calculate the total travel cost
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)