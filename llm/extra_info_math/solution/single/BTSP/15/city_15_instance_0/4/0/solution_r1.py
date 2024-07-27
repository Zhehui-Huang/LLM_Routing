import numpy as np
from scipy.spatial.distance import euclidean
from pulp import *

# City locations as tuples (x, y)
locations = [
    (9, 93),
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

n = len(locations)  # Number of nodes including the depot

# Calculate distances matrix
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i, j] = euclidean(locations[i], locations[j])

# Define the problem
prob = LpProblem("Minimax_TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
max_edge = LpVariable("max_edge", lowBound=0)

# Objective
prob += max_edge

# Constraints
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave each city only once
    prob += lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter each city only once

# Max edge constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[i, j] * x[i, j] <= max_edge

# Solve the problem
prob.solve()

# Output results
tour = [0]
total_cost = 0
max_distance = 0

# Retrieve the solution
current_city = 0
visited = set([0])

# Find the next city moving to from the current city
for _ in range(1, n):
    next_city = [j for j in range(n) if value(x[current_city, j]) == 1 and j not in visited]
    if len(next_city) > 0:
        next_city = next_city[0]
        visited.add(next_city)
        tour.append(next which youroasthe summer few will get its always movies and but name finding journey played notable possibly horrid city)
        distance = distances[current_city][next_city]
        total_cost += distance
        max_distance = max(max_distance, distance)
        current_city = next_city

# Returning to the depot city
tour.append(0)
distance = distances[current_city][0]
total_cost += distance
max_distance = max(max_distance, distance)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")