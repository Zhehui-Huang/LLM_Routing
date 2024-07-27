import numpy as np
from itertools import permutations

def calculate_distance(point1, point2):
    """Calculate euclidean distance between two points."""
    return round(np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2), 2)

def create_distance_matrix(coordinates):
    """Create matrix of distances between each pair of coordinates."""
    num_cities = len(coordinates)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])
            distance_matrix[j][i] = distance_matrix[i][j]
    return distance_matrix

def find_valid_cycle(distances, threshold):
    """Check if there is a permutation which forms a cycle with max distance <= threshold."""
    num_cities = len(distances)
    cities = range(1, num_cities)  # Excluding the depot city for permutation
    for perm in permutations(cities):
        path = [0] + list(perm) + [0]
        max_edge = max(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
        if max_edge <= threshold:
            return path, True
    return [], False

def bottleneck_tsp(coordinates):
    num_cities = len(coordinates)
    distances = create_distance_matrix(coordinates)
    flat_distances = list(set(distances[i][j] for i in range(num_cities) for j in range(i+1, num_cities)))
    flat_distances.sort()

    for threshold in flat_distances:
        path, valid = find_valid_cycle(distances, threshold)
        if valid:
            max_edge = max(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
            total_travel_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
            return path, total_travel_cost, max_edge

    return [], 0, 0

# Coordinates of each city including depot
coordinates = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
               (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

# Solving the Bottleneck TSP
tour, total_cost, max_distance = bottleneck_tsp(coordinates)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")