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
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the problem
problem = LpProblem("TSP", LpMinimize)

# Decision variables: x[i, j] is 1 if the tour goes directly from i to j, 0 otherwise
x = LpVariable.dicts("x", (range(n), range(n)), cat=LpBinary)

# Objective: minimize the maximum distance between consecutive cities
max_distance = LpVariable("max_distance")
problem += max_distance

# Add constraints
for i in range(n):
    problem += lpSum(x[i][j] for j in range(n) if j != i) == 1
    problem += lpSum(x[j][i] for j in range(n) if j != i) == 1
    for j in range(n):
        if i != j:
            problem += distances[i][j] * x[i][j] <= max_distance

# Subtour elimination
for r in range(2, n):
    for subset in combinations(range(n), r):
        problem += lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
problem.solve()

# Extract the solution
tour = []
for i in range(n):
    for j in range(n):
        if x[i][j].varValue > 0.99:
            tour.append((i, j))

# Order the tour starting from the depot
ordered_tour = []
if tour:
    current_city = 0
    ordered_tour.append(current_city)
    while len(ordered_tour) < n:
        next_cities = [j for i, j in tour if i == current_city]
        if next_cities:
            current_city = next_cities[0]
            ordered_tour.append(current_city)
    ordered_tour.append(0)  # Close the tour by returning to the depot

# Calculate the total travel cost and maximum distance
if ordered_tour:
    total_distance = sum(distances[ordered_tour[i]][ordered_tour[i + 1]] for i in range(len(ordered_tour) - 1))
    max_distance_value = max(distances[ordered_tour[i]][ordered_tour[i + 1]] for i in range(len(ordered_tour) - 1))
    print("Tour:", ordered_tour)
    print("Total travel cost:", total_distance)
    print("Maximum distance between consecutive cities:", max_distance_value)
else:
    print("No feasible tour was found.")