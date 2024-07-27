import numpy as. np
from mip import Model, xsum, minimize, BINARY, OptimizationStatus
from itertools import combinations

# Define coordinates of the cities
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

n = len(coordinates)  # Number of cities including the depot

# Calculate Euclidean distances between each pair of cities
dist = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist[i, j] = np.linalg.norm(np.array(coordinates[i]) - np.array(coordinates[j]))

# Initialize the model
model = Model()

# Variables x[i, j] - 1 if travel happens from city i to j, 0 otherwise
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]

# Auxiliary variable to help minimize the maximum distance traveled in a single move
max_dist = model.add_var()

# Objective: Minimize the maximum distance between consecutive cities in the tour
model.objective = minimize(max_dist)

# Each city is entered and left exactly once
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1
    model += xsum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination constraints
for S in range(3, n+1):
    for subset in combinations(range(1, n), S):
        model += xsum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Constraint to bind the maximum distance trip with our auxiliary variable
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i][j] * dist[i][j] <= max_dist

# Solve the problem
model.optimize()

# Check if the solution is optimal
if model.status == OptimizationStatus.OPTIMAL:
    tour = []
    max_distance = max_dist.x
    total_cost = 0
    for i in range(n):
        for j in range(n):
            if x[i][j].x >= 0.99:
                tour.append((i, j))
                total_cost += dist[i][j]

    decoded_tour = [0]
    current = 0
    while len(decoded_tour) < n:
        next_city = [j for i, j in tour if i == current][0]
        decoded_tour.append(next_city)
        current = next_city
    decoded_tour.append(0)  # end tour at the depot

    print("Tour:", decoded_tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("An optimal solution was not found.")