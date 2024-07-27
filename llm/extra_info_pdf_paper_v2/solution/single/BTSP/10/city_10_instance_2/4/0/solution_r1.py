import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define all city coordinates, including the depot
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distances between each pair of cities
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i, j] = euclidean(cities[i], cities[j])
    return distance_matrix

distance_matrix = calculate_distance_matrix(cities)  # Corrected the call to use the right function name

# Heuristic for BTSP
def find_btsp_tour(cities, distance_matrix):
    city_indices = list(range(1, len(cities)))  # exclude the depot (index 0)
    best_tour = None
    min_max_distance = float('inf')
    
    # Check all permutations of city visits
    for perm in permutations(city_indices):
        tour = [0] + list(perm) + [0]  # start and end at the depot
        max_edge_cost = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        if max_edge_cost < min_max_distance:
            min_max_distance = max_edge_cost
            best_tour = tour
    
    if best_tour is not None:
        total_cost = sum(distance_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))
        return best_tour, total_cost, min_max_distance
    else:
        return None, None, None

# Find the optimal BTSP tour
tour, total_travel_cost, max_distance = find_btsp_tour(cities, distance_matrix)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_travel****2**15**3cost])
print(" Maximum distance between consecutive cities:", max_distance)