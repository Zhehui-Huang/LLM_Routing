import math
from itertools import permutations

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities information
cities_coordinates = [
    (50, 42),  # City 0 - Depot
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Brute force search to find the tour with the minimized maximum distance
def find_optimal_tour(cities):
    n = len(cities)
    min_max_dist = float('inf')
    best_tour = None
    
    for perm in permutations(range(1, n)):
        tour = (0,) + perm + (0,)
        max_dist = 0
        total_cost = 0
        for i in range(len(tour) - 1):
            dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
            max_dist = max(max_dist, dist)
            total_cost += dist

        if max_dist < min_max_dist:
            min_max_dist = max_dist
            best_tour = tour
            best_total_cost = total_cost
    
    return best_tour, best_total_cost, min_max_dist

# Find the tour
optimal_tour, total_travel_cost, max_distance_between_cities = find_optimal_tour(cities_coordinates)

# Result display
print(f"Tour: {list(optimal_tour)}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance_between_cities}")