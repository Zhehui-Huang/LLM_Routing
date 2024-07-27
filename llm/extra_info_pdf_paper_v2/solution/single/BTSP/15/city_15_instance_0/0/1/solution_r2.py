import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50),
    (21, 23), (88, 59), (79, 77), (63, 23),
    (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

# Calculate the Euclidean distance between two city coordinates
def calculate_distances(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_population

distances = calculate_distances(cities)

# Function to find minimum maximum distance tour using brute force
def min_max_distance_tour(distances):
    n = len(distances)
    all_perms = permutations(range(1, n))  # Generate all permutations of city indices excluding the depot
    best_tour = None
    min_max_edge = float('inf')
    
    # Evaluate each permutation
    for perm in all_perms:
        tour = [0] + list(perm) + [0]  # Start and end at the depot (index 0)
        max_edge = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        if max_edge < min_max_edge:
            min_max_edge = max_edge
            best_tour = tour
    
    return best_tour, min_max_edge

best_tour, max_edge_length = min_max_distance_tour(distances)

# Calculate the total distance for the tour
def total_tour_distance(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

total_travel_cost = total_tour_distance(best_tour, distances)

# Printing results
print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_edge_length)