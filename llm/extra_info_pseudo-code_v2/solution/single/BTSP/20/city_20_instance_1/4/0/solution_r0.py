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
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_distances(cities):
    """Calculate the matrix of distances between each pair of cities."""
    n = len(cities)
    distance_matrix = {}
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(cities[i], cities[j])
            distance_matrix[(i, j)] = distance
            distance_matrix[(j, i)] = distance
    return distance_matrix

# Calculate distances between cities
distances = calculate_distances(cities_coords)

def find_bottleneck_tour(cities, distances):
    num_cities = len(cities)
    min_max_distance = float('inf')
    best_tour = None

    # Generate all possible tours (permutations); careful: computationally expensive!
    for perm in permutations(range(1, num_cities)):  # 0 is the depot city
        tour = [0] + list(perm) + [0]
        tour_distance = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
        max_distance = max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
            best_tour_distance = tour_distance

    return best_tour, best_tour_distance, min_max_distance

# Compute the bottleneck tour
bt_tour, bt_tour_distance, bt_tour_max_distance = find_bottleneck_tour(cities_coords, distances)

# Output results
print(f"Tour: {bt_tour}")
print(f"Total travel cost: {bt_tour_distance:.2f}")
print(f"Maximum distance between consecutive cities: {bt_tour_worst_distance:.2f}")