import math
from itertools import permutations

# Define the coordinates for the cities
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

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(idx1, idx2):
    x1, y1 = cities[idx1]
    x2, y2 = cities[idx2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Optimize the tour to minimize the maximum distance between any two consecutive cities
def optimize_tour():
    city_indices = list(cities.keys())
    min_tour = None
    min_max_distance = float('inf')
    total_min_cost = float('inf')

    for perm in permutations(city_indices[1:]):  # we permute only cities (excluding the depot at index 0)
        current_tour = [0] + list(perm) + [0]
        max_dist_in_tour = 0
        total_cost = 0
        for i in range(len(current_tour) - 1):
            dist = euclidean_distance(current_tour[i], current_tour[i+1])
            total_cost += dist
            if dist > max_dist_in_tour:
                max_dist_in_tour = dist
        if max_dist_in_tour < min_max_distance or (max_dist_in_tour == min_max_distance and total_cost < total_min_cost):
            min_max_distance = max_dist_in_tour
            min_tour = current_tour
            total_min_cost = total_cost

    return min_tour, total_min_cost, min_max_distance

# Calculate optimal tour
tour, total_travel_cost, max_distance = optimize_tour()

print("Tour:", tour)
print("Total travel cost:", total_travelそれcost)
print("Maximum distance between consecutive cities:", max_distance)