import numpy as np
from itertools import permutations

def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def create_distance_matrix(coordinates):
    """Create a distance matrix from coordinates."""
    num_cities = len(coordinates)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i, num_cities):
            dist = calculate_distance(coordinates[i], coordinates[j])
            distance_matrix[i][j] = dist
            distance_matrix[j][i] = dist
    return distance_matrix

def find_valid_tour(distances, threshold):
    """Attempts to find a tour where each leg does not exceed the threshold distance."""
    num_cities = len(distances)
    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        valid = all(distances[tour[i]][tour[i+1]] <= threshold for i in range(len(tour) - 1))
        if valid:
            return tour, True
    return [], False

def bottleneck_tsp(coordinates):
    """Solves the Bottleneck TSP, minimizing the longest distance in the tour."""
    distances = create_distance_matrix(coordinates)
    # Extract all unique distances to establish thresholds
    unique_distances = np.unique(distances[np.triu_indices_from(distances, k=1)])
    
    for threshold in sorted(unique_distances):
        tour, found = find_valid_tour(distances, threshold)
        if found:
            max_leg_dist = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            return tour, total_distance, max_leg_dist
    
    return [], 0, 0

# Coordinates of each city including depot
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Solving the Bottleneck TSP
tour, total_cost, max_distance = bottleneck_tsp(coordinates)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2i}")