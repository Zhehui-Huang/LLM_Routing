import math
from itertools import permutations

# Define the cities with their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute all distances between each pair of cities
def compute_distances():
    distances = {}
    for i in cities:
        for j in cities:
            if i != j:
                distances[(i, j)] = euclidean_distance(cities[i], cities[j])
    return distances

# Check if a specific path is valid within the given max distance
def is_valid_path(path, distances, max_dist):
    for i in range(len(path) - 1):
        if distances[(path[i], path[i + 1])] > max_dist:
            return False
    return True

# Attempt to find a Hamiltonian circuit given a max distance
def find_hamiltonian_path(distances, max_dist):
    for perm in permutations(range(1, len(cities))):  # all permutations of city indices except the depot
        path = [0] + list(perm) + [0]  # start and end at the depot
        if is_valid_path(path, distances, max_dist):
            return path
    return None

# Bottleneck Traveling Salesman Problem Solver
def bottleneck_tsp():
    distances = compute_distances()
    sorted_edges = sorted(distances.items(), key=lambda x: x[1])
    for edge, max_dist in sorted_edges:
        path = find_hamiltonian_path(distances, max_dist)
        if path:
            # Compute total cost and find max distance in the valid path
            total_cost = sum(distances[(path[i], path[i+1])] for i in range(len(path)-1))
            max_distance = max(distances[(path[i], path[i+1])] for i in range(len(path)-1))
            return path, total_cost, max_distance
    return None

# Use the bottleneck traveling salesman problem algorithm
result = bottleneck_tsp()

if result:
    tour, total_cost, max_distance = result
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No valid tour found.")