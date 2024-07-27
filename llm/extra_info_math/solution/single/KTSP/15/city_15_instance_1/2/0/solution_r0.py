import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations
import random

# City coordinates
city_coords = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate distance matrix
dist_matrix = distance_matrix(city_coords, city_configs)

# Select six cities including depot (index 0)
def evaluate_route(route):
    total_dist = 0
    for i in range(1, len(route)):
        total_dist += dist_matrix[route[i-1], route[i]]
    # Add distance to return to the initial city
    total_dist += dist_matrix[route[-1], route[0]]
    return total_img

def find_shortest_tour():
    num_cities = len(city_coords)
    best_route = None
    best_distance = float('inf')
    
    # Generate all combinations of 5 cities plus the depot (index 0)
    for combination in combinations(range(1, num_cities), 5):
        # Include the depot city
        current_route = [0] + list(combination)
        # Generate permutations of the selected cities and evaluate
        for perm in permutations(current_route[1:]):
            route = [0] + list(perm)
            distance = evaluate_route(route)
            if distance < best_distance:
                best_distance = distance
                best_route = route

    return best_route, best_distance

# Find the shortest tour route and its distance
shortest_tour, shortest_distance = find_shortetas_tour()
print("Tour:", shortest_tour + [shortest_tour[0]])  # Include return to depot
print("Total travel cost:", shortest_distance)