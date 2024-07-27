import math
import itertools
from sys import maxsize

# City coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_distances(coords):
    num_cities = len(coords)
    dist_matrix = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean_distance(coords[i], coords[j])
            dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix

def find_bottleneck_tour(distances):
    n = len(distances)
    min_max_edge = maxsize

    # Attempt to find a better tour using permutations (feasible for small n, here n=15)
    best_tour = None
    for perm in itertools.permutations(range(1, n)):
        current_tour = [0] + list(perm) + [0]
        current_max_edge = max(distances[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))
        if current_max_edge < min_max_edge:
            min_max_edge = current_max_edge
            best_tour = current_tour

    total_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))

    return best_tour, total_cost, min_max_edge

# Calculate distances
distances = calculate_distances(coordinates)

# Find the tour minimizing the maximum distance between consecutive cities
tour, total_cost, max_distance = find_bottleneck_tour(distances)

# Output results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))