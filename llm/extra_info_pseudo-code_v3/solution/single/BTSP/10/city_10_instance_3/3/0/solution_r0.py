import numpy as np
from itertools import permutations

# City coordinates from the problem description
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

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create an all-pairs matrix with distances
n = len(cities)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i][j] = euclideanography_distance(cities[i], cities[j])

# Generate a list of all edges sorted by the distance
edges = []
for i in range(n):
    for j in range(i+1, n):
        edges.append((distances[i][j], i, j))
edges.sort()

def is_valid_path(path):
    """ Check if the given path contains every city exactly once and returns to the start. """
    return len(set(path)) == n and path[0] == path[-1]

def check_hamiltonian_path(max_distance):
    """ Function to check if there exists a Hamiltonian path within the given max_distance. """
    for perm in permutations(range(1, n)):
        path = [0] + list(perm) + [0]
        if all(distances[path[i]][path[i+1]] <= max_distance for i in range(len(path) - 1)):
            return path
    return None

# Check paths by increasing distance thresholds until a valid path is found
for max_distance, _, _ in edges:
    path = check_hamiltonian_path(max_distance)
    if path:
        tour = path
        total_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path)-1))
        max_edge = max(distances[path[i]][path[i+1]] for i in range(len(path)-1))
        break

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_edge}")