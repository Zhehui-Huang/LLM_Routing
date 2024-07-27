import numpy as np
import math
from itertools import permutations

# Coordinates of cities including the depot
cities = [
    (54, 87),  # depot city 0
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# Calculating Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create a matrix of all distances
num_cities = len(cities)
dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Function to find the best BTSP tour using brute force approach, minimizing the maximum distance
def find_optimal_btsp_tour(dist_matrix):
    min_max_distance = float('inf')
    best_tour = None
    all_permutations = permutations(range(1, num_cities))  # Exclude the depot (0) for permutations
    for perm in all_permutations:
        tour = [0] + list(perm) + [0]  # start and end at the depot
        max_edge_cost = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        if max_edge_cost < min_max_distance:
            min_max_distance = max_edge_cost
            best_tour = tour
    
    total_cost = sum(dist_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))
    return best_tour, total_cost, min_max_distance

best_tour, best_total_distance, best_max_distance = find_optimal_btsp_tour(dist_matrix)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_distance, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))