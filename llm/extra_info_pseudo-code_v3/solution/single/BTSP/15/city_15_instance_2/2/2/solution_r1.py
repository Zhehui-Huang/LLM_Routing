import numpy as np
from itertools import permutations

def calculate_distance(point1, point2):
    """Calculate euclidean distance between two points."""
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def create_distance_matrix(coordinates):
    """Create matrix of distances between each pair of coordinates."""
    num_cities = len(coordinates)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])
    return distance_matrix

def max_constrained_hamiltonian_path(distances, threshold):
    """Check if there exists a permutation of cities such that no edge in the tour exceeds the threshold."""
    n = len(distances)
    for perm in permutations(range(1, n)):
        perm = list(perm)
        max_distance = max(distances[0][perm[0]], distances[perm[-1]][0])
        valid = True
        for i in range(len(perm)-1):
            if distances[perm[i]][perm[i+1]] > threshold:
                valid = False
                break
            max_distance = max(max_distance, distances[perm[i]][perm[i+1]])
        if valid and max_distance <= threshold:
            return [0] + perm + [0], True
    return [], False

def bottleneck_tsp(coordinates):
    """Find a Hamiltonian cycle such that the maximum distance between consecutive cities is minimized."""
    distances = create_distance_matrix(coordinates)
    all_edges = set(distances[i][j] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)
    sorted_edges = sorted(all_edges)

    for threshold in sorted_edges:
        tour, found = max_constrained_hamiltonian_path(distances, threshold)
        if found:
            total_travel_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            return tour, total_travel_cost, threshold

    return [], 0, 0

# Coordinates of each city including depot
coordinates = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
               (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

# Solving the Bottleneck TSP
tour, total_cost, max_distance = bottleneck_tsp(coordinates)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")