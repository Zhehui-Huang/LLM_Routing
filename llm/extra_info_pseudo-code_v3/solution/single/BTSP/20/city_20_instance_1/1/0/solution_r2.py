import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_tour(coords):
    num_cities = len(coords)
    # Create all permutations of city indices, excluding the depot (index 0)
    perms = permutations(range(1, num_cities))
    best_tour = None
    best_max_dist = float('inf')
    best_total_dist = 0

    # Evaluate each permutation
    for perm in perms:
        # Construct the path: start at depot, visit cities in permutation, return to depot
        path = [0] + list(perm) + [0]
        # Calculate maximum distance between consecutive cities
        max_dist = max(calculate_distance(coords[path[i]], coords[path[i+1]]) for i in range(len(path) - 1))
        total_dist = sum(calculate_distance(coords[path[i]], coords[path[i+1]]) for i in range(len(path) - 1))
        
        if max_dist < best_max_dist:
            best_max_dist = max_dist
            best_total_dist = total_dist
            best_tour = path

    return best_tour, best_total_dist, best_max_dist

# Coordinates of the cities including depot
coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

# Finding the tour
tour, total_dist, max_dist = find_tour(coords)

print("Tour:", tour)
print("Total travel cost:", total_dist)
print("Maximum distance between consecutive cities:", max_dist)