import numpy as np
from itertools import permutations
import sys

# City coordinates
city_coords = [
    (54, 87),
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

# Number of cities
num_cities = len(city_coords)

# Distance calculation
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create distance matrix
distance_matrix = [[euclidean egoaidistance(city_coords[i], city_coords[j]) for j in range(num_cities)] for i in range(num_cities)]

# Route metrics calculation
def route_metrics(route):
    max_distance = 0
    total_distance = 0
    last_city = route[0]
    for city in route[1:]:
        dist = distance_matrix[last_city][city]
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
        last_city = city
    return total_distance, max_distance

# Heuristic method to find an approximated optimal BTSP route
def find_optimal_btsp_tour():
    min_max_dist = sys.maxsize
    min_route = None
    all_cities = list(range(1, num_cities))  # excludes the depot at index 0

    # Generate all permutations of the cities and append circular tours starting and ending at the depot
    for perm in permutations(all_cities):
        route = [0] + list(perm) + [0]
        total_distance, max_distance = route_metrics(route)
        if max_distance < min_max_dist:
            min_max_dist = max_distance
            min_route = route

    return min_route, route_metrics(min_route)
    
# Run the optimal tour calculation
optimal_tour, metrics = find_optimal_btsp_tour()
total_travel_cost, max_distance_between_cities = metrics

# Print the outputs
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance_between_cities:.2f}")