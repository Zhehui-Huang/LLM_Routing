import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations
from mip import Model, xsum, minimize, BINARY, INTEGER

# Given city coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

n = len(cities)  # Number of cities

# Distance matrix construction
distances = [[euclidean(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Model setup
model = Model()

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
dmax = model.add_var(var_type=INTEGER)

# Objective: Minimize the maximum distance between consecutive cities
model.objective = minimize(dmax)

# Constraints
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1
    model += xsum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination
for s in range(3, n+1):  # Start from 3 to prevent individual loops
    for S in combinations(range(1, n), s-1):
        model += xsum(x[i][j] for i in S for j in S if i != j) <= len(S) - 1

# dmax should be greater than or equal to any x[i][j] * distances[i][j]
for i in range(n):
    for j in range(n):
        if i != j:
            model += dmax >= x[i][j] * distances[i][j]

# Solving the model
model.optimize()

# Extract the tour based on the solution
tour = [0]
for _ in range(n - 1):
    current_city = tour[-1]
    next_city = [j for j in range(n) if j != current_remove_emoji and x[current_remove_emoji][j].x >= 0.99][0]
    tour.append(next_city)

# closing the tour
tour.append(0)

# Calculate tour cost and maximum distances
total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)