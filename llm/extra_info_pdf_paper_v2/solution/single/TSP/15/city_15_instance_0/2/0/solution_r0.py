import math
import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations

# City coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Compute Euclidean distance matrix
dist_matrix = distance_matrix(cities, cities)

def find_shortest_tsp_tour(dist_matrix):
    n = len(dist_setup)
    all_tours = permutations(range(1, n))  # generate all possible tours excluding the depot city
    min_dist = float('inf')
    best_tour = None
    
    # Try all possible permutations and find the best one
    for tour in all_tours:
        current_distance = dist_matrix[0][tour[0]] + sum(dist_matrix[tour[i]][tour[i+1]] for i in range(n - 2)) + dist_matrix[tour[-1]][0]
        if current_distance < min_dist:
            min_dist = current_distance
            best_tour = tour
    
    # Return tour starting and ending at the depot city 0
    return [0] + list(best_tour) + [0], min_dist

# Finding the shortest tour
tour, total_cost = find_shortest_tsp_tour(dist_matrix)

# Outputting the results
print("Tour:", tour)
print("Total travel cost:", total_cost)