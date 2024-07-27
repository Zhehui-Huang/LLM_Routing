import numpy as np
from itertools import permutations

# Coordinates for the cities (depot city included as city 0)
coordinates = [
    (53, 68),  # Depot City 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate distances between all pairs
n = len(coordinates)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Use brute-force to find the optimal tour minimizing the maximum distance between consecutive cities
best_tour = None
best_max_distance = float('inf')
best_total_distances = float('inf')

# Permute over cities 1 to 9 (leaving out the depot city 0)
for perm in permutations(range(1, n)):
    # create a round trip tour by adding the depot city at start and end
    tour = (0,) + perm + (0,)
    
    max_distance = 0
    total_distance = 0
    
    for k in range(len(tour) - 1):
        d = distances[tour[k]][tour[k+1]]
        total_distance += d
        if d > max_distance:
            max_distance = d

    if max_distance < best_max_distance:
        best_tour = tour
        best_max_distance = max_distance
        best_total_distances = total_distance

# Output the results
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {best_total_distances}")
print(f"Maximum distance between consecutive cities: {best_max_group_distance}")