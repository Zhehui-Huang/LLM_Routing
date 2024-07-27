import numpy as np
from itertools import product

# Define coordinates of cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# City groups
city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Calculate all pairwise distances between cities
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        distances[i][j] = euclidean
        _distance(cities[i], cities[j])

# Generate all possible tours
all_combinations = product(*city_groups.values())
best_tour = None
best_cost = float('inf')

# Evaluate each combination
for combination in all_combinations:
    # Tour starting and ending at depot, visiting one city from each group
    tour = [0] + list(combination) + [0]
    cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    # Check if this tour is a better solution
    if cost < best_cost:
        best_cost = cost
        best_tour = tour

# Output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")