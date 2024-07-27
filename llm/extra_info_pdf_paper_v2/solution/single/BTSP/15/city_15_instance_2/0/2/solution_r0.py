import math
from scipy.spatial import distance_matrix
import numpy as np
from itertools import permutations

# Define cities' coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Bottleneck TSP approach
def bottleneck_tsp(distances):
    n = len(distances)
    min_max_distance = float('inf')
    best_tour = None

    # Permute through cities (0 must be at the start and end, exclude 0 in permutations)
    for perm in permutations(range(1, n)):
        full_cycle = [0] + list(perm) + [0]
        # Calculate the maximum edge weight in this permutation
        max_distance_in_tour = max(distances[full_cycle[i]][full_cycle[i+1]] for i in range(len(full_cycle) - 1))
        total_distance = sum(distances[full_cycle[i]][full_cycle[i+1]] for i in range(len(full_cycle) - 1))
        if max_distance_in_tour < min_max_distance:
            min_max_distance = max_distance_in_tour
            best_tour = full_cycle
            best_total_distance = total_distance
    
    return best_tour, best_total_distance, min_max_distance

# Get the best tour minimizing the maximum distance between any two consecutive cities
best_tour, best_total_distance, best_max_distance = bottleneck_tsp(dist_matrix)

# Output
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_distance, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))