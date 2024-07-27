from scipy.spatial.distance import pdist, squareform
import numpy as np
from itertools import permutations

# Defining the cities' coordinates
coordinates = np.array([
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
])

# Calculate the Euclidean distances matrix
dist_matrix = squareform(pdist(coordinates, metric='euclidean'))

def total_distance(tour):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Generate all possible tours from the depot (excluding depot itself)
cities = list(range(1, len(coordinates)))
min_tour = None
min_cost = float('inf')

# Iterate through all permutations of the cities to find the shortest tour
for perm in permutations(cities):
    # Create the full tour from depot to cities and return to depot
    full_tour = [0] + list(perm) + [0]
    cost = total_distance(full_tour)
    if cost < min_cost:
        min_tour = full_tour
        min_cost = cost

print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")