import math
from itertools import permutations

# Define cities' coordinates
cities_coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances between cities
def calculate_distances(cities):
    distances = {}
    n = len(cities)
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[(i, j)] = euclidean_distance(cities[i], cities[j])
    return distances

distances = calculate_distances(cities_coords)

# Generate all possible tours using permutations
def find_optimal_tour():
    num_cities = len(cities_coords)
    best_tour = None
    min_bottleneck = float('inf')
    best_total_distance = 0
    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        max_edge_length = max(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
        total_distance = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
        
        if max_edge_length < min_bottleneck:
            min_bottleneck = max_edge_length
            best_tour = tour
            best_total_distance = total_distance

    return best_tour, best_total_distance, min_bottleneck

# Compute the best tour minimizing the maximum consecutive distance
tour, total_distance, max_distance_between_cities = find_optimal_tour()

# Display the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance_between_cities:.2f}")