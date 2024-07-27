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

# Subtour elimination constraints (SECs)
for k in range(2, n):
    for S in combinations(range(n), k):
        prob += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Output results
tour = []
total_cost = 0
max_distance = 0

# Retrieve the solution
current_city = 0
while True:
    next_cities = [j for j in range(n) if j != current_city and value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

tour = [0] + tour + [0]
for i in range(1, len(tour)):
    distance = distances[tour[i-1], tour[i]]
    total_cost += distance
    if distance > max_distance:
        max_distance = distance

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")