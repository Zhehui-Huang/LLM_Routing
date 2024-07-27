import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations, permutations

# Coordinates of the cities
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Distance calculation function
def distance(pt1, pt2):
    return euclidean(pt1, pt2)

# Generate distance matrix
dist_matrix = np.zeros((15, 15))
for i in range(15):
    for j in range(15):
        dist_matrix[i, j] = distance(coordinates[i], coordinates[j])

# Select k-1 additional cities since depot is included (total k = 10)
best_tour = None
min_cost = float('inf')

# Iterate over combinations of cities (excluding depot which is city 0)
for cities in combinations(range(1, 15), 9):
    # Check permutations of this combination
    for perm in permutations(cities):
        # Create a complete tour starting and ending at the depot (city 0)
        tour = [0] + list(perm) + [0]
        
        # Calculate the cost of this tour
        cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
        
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Display the results
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))