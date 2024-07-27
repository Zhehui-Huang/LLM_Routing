import numpy as np
from itertools import permutations

# Define the city positions
cities = [
    (16, 90),  # City 0 - Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 78)   # City 14
]

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return np.hypot(c1[0] - c2[0], c1[1] - c2[1])

# Matrix of distances between each pair of cities
n = len(cities)
distances = np.array([[euclidean_header(cities[i], cities[j]) for j in range(n)] for i in range(n)])

# Minimum Bottleneck Hamiltonian Cycle (Brute Force Approach for small instances)
min_max_distance = float('inf')
best_path = None
total_cost = 0

# Generate all permutations of cities (excluding the depot city 0)
for perm in permutations(range(1, n)):
    # Include the depot at start and end
    tour = (0,) + perm + (0,)
    
    # Maximum distance in this tour
    max_distance_in_tour = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    # Check if this tour has a smaller max distance bottleneck
    if max_distance_in_tour < min_max_distance:
        min_max_distance = max_distance_in_tour
        best_path = tour
        total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output results
if best_path:
    print("Tour:", list(best_path))
    print("Total travel cost:", round(total_cost, 2))
    print("Maximum distance between consecutive cities:", round(min_max_distance, 2))
else:
    print("No valid tour found")