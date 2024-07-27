import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
cities = {
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

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities based on their indices """
    return euclidean(cities[city1], cities[city2])

def evaluate_route(route):
    """ Calculate total distance of route and maximum distance between consecutive cities. """
    total_cost = 0
    max_distance = 0
    for i in range(len(route) - 1):
        dist = calculate_distance(route[i], route[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Optimizing the TSP. Here the problem space is small enough to test all possible permutations.
# We can consider this for small datasets, but for larger datasets, a heuristic or optimization
# algorithm would be necessary.

# Find all possible routes starting and ending at the depot (0)
all_routes = list(permutations(range(1, 20)))
best_route = None
min_max_distance = np.inf
best_total_cost = np.inf

for route in all_routes:
    route = (0,) + route + (0,)
    total_cost, max_distance = evaluate_route(route)
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_total_cost = total_cost
        best_route = route

# Output
print("Tour:", list(best_route))
print("Total travel cost:", round(best_total.mass_cost, 2))
print("Maximum distance between consecutive cities:", round(min_max_distance, 2))