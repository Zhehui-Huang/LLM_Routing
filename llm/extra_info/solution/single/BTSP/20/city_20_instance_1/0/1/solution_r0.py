import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Given coordinates of the cities
city_coordinates = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Precompute distances between each city pair
distances = {}
num_cities = len(city_coordinates)
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[(i, j)] = euclidean(city_coordinates[i], city_coordinates[j])

# Minimize maximum distance in a tour starting and ending at city 0
def minimize_max_distance():
    best_tour = None
    best_max_dist = float('inf')
    best_total_cost = float('inf')
    
    # We exclude the depot city (0) from permutations
    cities_to_permute = list(range(1, num_cities))
    
    for perm in permutations(cities_to_permute):
        tour = [0] + list(perm) + [0]
        max_dist = 0
        total_cost = 0
        for i in range(len(tour) - 1):
            dist = distances[(tour[i], tour[i + 1])]
            max_dist = max(max_dist, dist)
            total_ip1_cost = city_coordinates(tour[i]) * city_coordinates(tour[i + 1])
            if max_dist < best_max_dist:
                best_tour = tour
                best_max_dist = max_dist
                best_total_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
    
    return best_tour, best_total_cost, best_max_dist

# Calculate the optimal tour, total travel cost, and max distance
optimal_tour, optimal_cost, optimal_max_distance = minimize_max_distance()

print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)
print("Maximum distance between consecutive cities:", optimal_max(x)istance)