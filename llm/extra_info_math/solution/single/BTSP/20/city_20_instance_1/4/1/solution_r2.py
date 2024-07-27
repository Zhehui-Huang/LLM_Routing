from scipy.spatial import distance
import numpy as np
from mip import Model, xsum, BINARY, minimize, OptimizationStatus

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
            distances[i][j] = float('inf')  # Use 'inf' to prevent choosing the same city

# Create optimization model
model = Model()

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
u = [model.add_var(lb=1, ub=n-1) for i in range(1, n)]
u = [0] + u  # Depot does not need a subtour elimination variable

# Objective: minimize the maximum travel distance in any part of the tour
max_dist = model.add_var()
model += minimize(max_dist)

# Constraints
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if j != i) == 1
    model += xsum(x[j][i] for j in range(n) if j != i) == 1

# Distance constraints related to objective
for i in range(n):
    for j in range(n):
        if i != j:
            model += max_dist >= x[i][j] * distances[i][j]

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n) * x[i][j] <= n - 1

# Solve the model
model.optimize()

# Extract the solution
if model.num_solutions:
    tour = []
    next_city = 0
    for _ in range(n):
        for j in range(n):
            if x[next_city][j].x >= 0.99:
                tour.append(next_city)
                next_city = j
                break
    tour.append(0)  # Return to depot

    # Calculate the total cost and max distance between consecutive cities
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No solution found.")