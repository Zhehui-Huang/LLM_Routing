import numpy as np
from itertools import permutations

# List of cities coordinates
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Number of cities
n = len(cities)

# Compute Euclidean distances between each pair of cities
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i][j] = distance(cities[i], cities[j])

# --------- Problem Part ---------
# Initialize minimum max distance very high
min_max_distance = float('inf')
best_tour = None

# Brute force attempt to find the best tour minimizing the maximum distance
# across consecutive cities
for perm in permutations(range(1, n)):  # Generate all permutations of n-1 cities, excluding the depot (0)
    tour = [0] + list(perm) + [0]
    max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    if max_distance < min_max_distance:
        min_max_idstance = max_distance
        best_tour = tour
        best_total_distance = total_distance

# Assuming 'best_tour' is the tour minimizing the maximum distance across consecutive cities
print("Tour:", best_tour)
print("Total travel cost:", best_total_distance)
print("Maximum distance between consecutive cities:", min_max_distance)