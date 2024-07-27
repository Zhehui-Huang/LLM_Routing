import math
import networkx as nx
from itertools import permutations

# City coordinates
coords = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)

# Generate all permutations of cities, excluding the starting depot city
city_indices = list(coords.keys())
city_indices.remove(0)
tours = permutations(city_indices)

# Function to find the minimum maximum leg distance tour
def find_optimal_tour():
    min_max_distance = float('inf')
    best_tour = None

    # Check each permutation of cities
    for perm in tours:
        current_tour = [0] + list(perm) + [0]
        max_leg_distance = max(euclidean_distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
        
        if max_leg_distance < min_max_distance:
            min_max_distance = max_leg_distance
            best_tour = current_tour

    return best_tour, min_max_distance

# Calculate optimal tour and min max distance
optimal_tour, min_max_distance = find_optimal_tour()

# Compute the total travel distance for the tour
total_travel_cost = sum(euclidean_distance(optimal_tour[i], optimal_tour[i + 1]) for i in range(len(optimal_tour) - 1))

# Preparing final output
output = {
    "Tour": optimal_tour,
    "Total travel cost": total_travel_cost,
    "Maximum distance between consecutive cities": min_max_distance
}

print(output)