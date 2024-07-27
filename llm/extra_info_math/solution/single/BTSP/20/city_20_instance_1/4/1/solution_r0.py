from scipy.spatial import distance
import numpy as np
from itertools import combinations
from mip import Model, xsum, minimize, BINARY, MAXIMIZE

# Define the cities and their coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}
n = len(cities)

# Calculate distances between each pair of cities
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = distance.euclidean(cities[i], cities[j])
        else:
            distances[i][j] = float('inf')  # Inf for same city distance to avoid cycles in the same city

# Optimization model
model = Model()

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(n)]  # helper variables for subtour elimination

# Objective: minimize the maximum distance used in the tour
M = model.add_var()
model.objective = minimize(M)

# Constraints
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1
    model += xsum(x[j][i] for j in range(n) if i != j) == 1

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += M >= distances[i][j]*x[i][j]

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n-1)*x[i][j] <= n-2

# Solve model
model.optimize(max_seconds=300)  # Adjust the maximum computation time based on complexity

# Check if a solution was found
if model.num_solutions:
    tour = []
    for i in range(n):
        for j in range(n):
            if x[i][j].x >= 0.99:
                tour.append((i, j))

    # Organize the tour starting from depot
    current = 0
    visited = set()
    organized_tour = [0]
    while len(organized_tour) < n:
        for i, j in tour:
            if i == current and j not in visited:
                organized_tour.append(j)
                visited.add(j)
                current = j
                break
    organized_tour.append(0)  # return to depot

    # Calculate total cost and max distance
    total_cost = sum(distances[organized_tour[i]][organized_tour[i+1]] for i in range(len(organized_tour)-1))
    max_dist = max(distances[organized_tour[i]][organized_tour[i+1]] for i in range(len(organized_tour)-1))

    # Output
    output = {
        "Tour": organized_tour,
        "Total travel cost": total_cost,
        "Maximum distance between consecutive cities": max_dist
    }
    print(output)
else:
    print("No solution found within the given computation time.")