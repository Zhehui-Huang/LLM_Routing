import math
from itertools import permutations

# City coordinates indexed from city 0 (Depot) to city 19.
city_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def compute_distance(coord1, coord2):
    """Compute Euclidean distance between two cities given their coordinates."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Precompute distances between all pairs of cities.
num_cities = len(city_coordinates)
distances = [
    [compute_distance(city_coordinates[i], city_coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)
]

def find_bottleneck_tour():
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')
    
    # Generating all permutations of city indices, excluding city 0.
    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        max_distance = max(
            distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)
        )
        total_cost = sum(
            distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)
        )
        
        # Checking if the current permutation gives a better maximum distance.
        if max_distance < best_max_distance:
            best_max_distance = max_distance
            best_total_cost = total_cost
            best_tour = tour
    
    return best_tour, best_total_cost, best_max_distance

# Execute the function to find the optimal path
result_tour, result_total_cost, result_max_distance = find_bottleneck_tour()

print(f"Tour: {result_tour}")
print(f"Total travel cost: {result_total_cost}")
print(f"Maximum distance between consecutive cities: {result_max_distance}")