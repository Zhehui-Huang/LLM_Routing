import numpy as np
from itertools import permutations

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Number of cities
n = len(cities)

# Function to calculate Euclidean distances
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate and initialize distance matrix
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Generate list of all edges organized by distances
edges = [(distances[i][j], i, j) for i in range(n) for j in range(i + 1, n)]
edges.sort()

# Function to check for a Hamiltonian path with a given maximum edge length
def path_exists(max_len):
    # Check all permutations of cities excluding the depot city
    for perm in permutations(range(1, n)):
        path = [0] + list(perm) + [0]
        max_edge_length = max(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
        if max_edge_length <= max_len:
            return path, max_edge_length
    return None, None

# Main loop to find the minimum bottleneck tour
for edge_length, _, _ in edges:
    path, max_edge_length = path_exists(edge_length)
    if path is not None:
        tour = path
        total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        print(f"Tour: {tour}")
        print(f"Total travel cost: {total_cost:.2f}")
        print(f"Maximum distance between consecutive cities: {max_edge_length:.2f}")
        break