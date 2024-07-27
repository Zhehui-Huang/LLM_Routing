import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of cities
city_coords = [
    (30, 56),
    (53, 42),
    (1, 95),
    (25, 61),
    (69, 57),
    (6, 58),
    (12, 84),
    (72, 77),
    (98, 95),
    (11, 0),
    (61, 25),
    (52, 0),
    (60, 95),
    (10, 94),
    (96, 73),
    (14, 47),
    (18, 16),
    (4, 43),
    (53, 76),
    (19, 72)
]

# Number of cities
num_cities = len(city_coords)

# Calculate Euclidean distances between all pairs of cities
distances = {}
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean(city_coords[i], city_coords[j])
        distances[(i, j)] = dist
        distances[(j, i)] = dist

# Sort distances based on their length
sorted_distances = sorted(distances.items(), key=lambda x: x[1])

def find_hamiltonian_path(max_edge_weight):
    # Check if a Hamiltonian path can be formed with edge constraint max_edge_weight
    graph = {i: [] for i in range(num_cities)}
    for (u, v), d in distances.items():
        if d <= max_edge_weight:
            graph[u].append(v)
            graph[v].append(u)
    
    for perm in permutations(range(1, num_cities)):
        full_path = [0] + list(perm) + [0]
        valid_path = True
        max_edge = 0
        for k in range(len(full_path) - 1):
            if full_path[k+1] not in graph[full_path[k]]:
                valid_path = False
                break
            edge_weight = distances[(full_path[k], full_path[k+1])]
            max_edge = max(max_edge, edge_weight)
        if valid_path:
            return True, full_path, max_edge
    return False, [], 0

def bottleneck_tsp():
    for edge, weight in sorted_distances:
        valid, path, max_edge = find_hamiltonian_path(weight)
        if valid:
            total_cost = sum(distances[(path[i], path[i+1])] for i in range(len(path)-1))
            return path, total_cost, max_edge
    return [], 0, 0

tour, total_cost, max_distance = bottleneck_tsp()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")