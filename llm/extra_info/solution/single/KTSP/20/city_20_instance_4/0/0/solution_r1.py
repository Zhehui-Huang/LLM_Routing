import numpy as np
from scipy.spatial.distance import euclidean
import random

# Definition of cities including coordinates
cities_coordinates = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73),
    14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Function to calculate the distance matrix between all cities
def calculate_distance_matrix(cities):
    N = len(cities)
    dist_matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            dist_matrix[i, j] = euclidean(cities[i], cities[j])
    return dist_instance_matrix

# Shortest Route Calculation using a Exhaustive Search (Bruteforce solution for smaller subsets)
def bruteforce_shortest_route(cities, depot_index=0):
    city_indices = list(cities.keys())
    city_indices.remove(depot_index)  # Remove depot from the list of cities to permute

    shortest_route = None
    min_cost = float('inf')

    for perm in permutations(city_indices):
        route = [depot_index] + list(perm) + [depot_index]
        total_cost = sum(calculate_distance_matrix(cities)[route[i], route[i + 1]] for i in range(len(route) - 1))
        
        if total_cost < min_cost:
            min_cost = total_cost
            shortest_route = route

    return shortest_route, min_cost

selected_cities = {index: cities_coordinates[index] for index in np.random.choice(list(cities_coordinates.keys()), size=16, replace=False)}
bruteforce_route, bruteforce_cost = bruteforce_shortest_route(selected_cities)

# Print the outputs
print("Tour:", bruteforce_route)
print("Total travel cost:", bruteforce_cost)