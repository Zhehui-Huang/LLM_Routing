import numpy as np
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary
from itertools import combinations
import math

# Cities coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

n = len(cities)

# Calculate distances between all cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the problem
problem = LpProblem("TSP", LpMinimize)

# Decision variables: x[i, j] is 1 if the tour goes directly from i to j, 0 otherwise
x = LpVariable.dicts("x", (range(n), range(n)), cat=LpBinary)

# Objective: minimize the maximum distance traveled between two consecutive cities
max_distance = LpVariable("max_distance")
problem += max_distance

# Constraints
for i in range(n):
    problem += lpSum(x[i][j] for j in range(n) if j != i) == 1  # leave each city once
    problem += lpSum(x[j][i] for j in range(n) if j != i) == 1  # enter each city once

# Max distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            problem += distances[i][j] * x[i][j] <= max_distance

# Subtour elimination
for r in range(2, n):
    for subset in combinations(range(n), r):
        problem += lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
problem.solve()

# Retrieve the tour from variables
tour = []
current_city = 0
visited = [False] * n
for _ in range(n):
    visited[current_city] = True
    for j in range(n):
        if int(x[current_city][j].varValue) == 1 and not visited[j]:
            tour.append(j)
            current_city = j
            break

# Closing the tour by returning to the starting depot city
tour = [0] + tour + [0]

# Calculate the total travel cost and maximum distance
total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance_value = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance_value)