import math
from itertools import permutations

# Define the cities coordinates
cities = [
    (50, 42),  # Depot
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Find the path with minimized maximum distance between consecutive cities
def find_min_max_tour(cities):
    num_cities = len(cities)
    # Generate all possible tours starting and ending at the depot, sorting by the maximum leg distance
    best_tour = None
    best_max_dist = float('inf')
    total_best_cost = float('inf')

    # Permute over other cities (excluding depot)
    for perm in permutations(range(1, num_cities)):
        current_tour = [0] + list(perm) + [0]  # start and end at the depot
        current_distances = [euclidean_distance(cities[current_tour[i]], cities[current_tour[i + 1]]) for i in range(len(current_tour) - 1)]
        max_dist = max(current_distances)
        total_cost = sum(current_distances)
        if max_dist < best_max_dist or (max_dist == best_max_dist and total_cost < total_best_cost):
            best_tour = current_tour
            best_max_dist = max_dist
            total_best_cost = total_cost
            
    return best_tour, total_best_cost, best_max_dist

# Compute the tour
tour, total_cost, max_distance = find_min_max_tour(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)