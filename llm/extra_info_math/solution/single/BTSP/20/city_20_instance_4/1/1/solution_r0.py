import math
from pulp import *
import numpy as np

# Define the coordinates of the depot and cities
coordinates = [
    (26, 60),  # Depot
    (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50),
    (60, 29), (29, 26), (85, 68), (60, 1),
    (71, 73), (82, 47), (19, 25), (75, 9),
    (52, 54), (64, 72), (14, 89)  # City 19
]

# Number of cities including the depot
n = len(coordinates)

# Calculate Euclidean distance between two points
def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
distances = [[euclidean_dist(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setting up the problem
prob = LpProblem("Minimax_TSP", LpMinimize)
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], 0, 1, LpBinary)

# Objective function: Minimize the maximum distance between any two consecutive cities
max_var = LpVariable("max_distance")
prob += max_var

# Constraints for visiting each city exactly once
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1

for j in range(n):
    prob += lpSum(x[(i, j)] for i in range(n) if i != j) == 1

# Eliminate subtours
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        prob += lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Link the distance with decision variables
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[(i, j)] * distances[i][j] <= max_var

# Solve the problem
prob.solve()

# Extract the solution and print the results
tour = []
max_distance = 0
total_cost = 0

# Find the start point of the tour
for j in range(n):
    if x[(0, j)].varValue == 1:
        tour.append(0)
        tour.append(j)
        break

# Follow the tour until return to the start point
while tour[-1] != 0:
    i = tour[-1]
    for j in range(n):
        if x[(i, j)].varValue == 1 and j not in tour:
            tour.append(j)
            total_cost += distances[i][j]
            max_distance = max(max_distance, distances[i][j])
            break

total_cost += distances[tour[-1]][0]  # Add the last leg back to the depot
max_distance = max(max_distance, distances[tour[-1]][0])
tour.append(0)  # Complete the tour by returning to the depot

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)