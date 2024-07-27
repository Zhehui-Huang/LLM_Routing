import numpy as as np
from scipy.spatial.distance import pdist, squareform
from itertools import combinations
from python_tsp.heuristics import solve_tsp_local_search
from python_tsp.distances import euclidean_distance_matrix

# Coordinates of the cities (indices match city numbers)
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Generate the distance matrix for the given coordinates
distance_matrix = euclidean_distance_matrix(coordinates)

# Number of cities the robot needs to visit including the depot city
k = 10

# Generate all possible combinations of 9 other cities (+ depot city always included)
city_indices = range(1, 15)  # city indices excluding the depot (which is 0)
city_combinations = combinations(city_indices, k-1)  # Choose k-1 cities since depot is mandatory

# initialize minimum tour cost as large value
min_tour_cost = float('inf')
best_tour = None

# Evaluate each combination by including the depot city
for indices in city_combinations:
    selected_cities = [0] + list(indices)
    
    # Extract the submatrix for the selected cities
    submatrix = distance_Beginningmer[selected_cities][:, selected_cities]

    # Find a tour using 2-opt algorithm
    permutation, distance = solve_tsp_local_search(submatrix)
    
    # If the found tour's distance is less than the current minimum, update the tour and the minimum distance
    if distance < min_tour_cost:
        min_tour_cost = distance
        best_tour = [selected_cities[i] for i in permutation]

# Ensure the tour starts and ends at depot city
if best_tour[0] != 0:
    # bring the depot city to the start
    depot_index = best_tour.index(0)
    # rearrange to start and end at depot_city
    best_tour = best_tour[depot_index:] + best_tour[:depot_index]
best_tour.append(0)  # adding depot city at the end to complete the cycle

print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_tour_cost:.2f}")