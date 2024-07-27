import math
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpBinary
import itertools

# City coordinates given
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), 
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

n = len(coordinates)  # Number of cities including the depot

# Calculate Euclidean Distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost matrix for traveling from each city to each other city
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem setup
prob = LpProblem("TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i,j) for i in range(n) for j in range(n)], cat=LpBinary)

# Objective
prob += lpSum(x[i, j] * cost[i][j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if j != i) == 1  # leave each city i exactly once
    prob += lpSum(x[j, i] for j in range(n) if j != i) == 1  # enter each city i exactly once

# Subtour elimination constraints (SEC)
for s in range(3, n):
    for S in itertools.combinations(range(1, n), s):
        prob += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solving the problem
prob.solve()

# Getting results
tour = []
visited = [0]  # start from the depot city
while len(visited) < n:
    for j in range(n):
        if x[visited[-1], j].varValue == 1:
            tour.append(j)
            visited.append(j)
            break
tour.append(0)  # return to the depot city
total_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)