import math
from itertools import permutations

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def find_hamiltonian_path(bottleneck_graph, start, all_nodes):
    n = len(all_nodes)
    paths = [(start, [start], set([start]))]
    while paths:
        city, path, visited = paths.pop()
        if len(path) == n:
            if start in bottleneck_graph[city]: # To ensure it forms a cycle with the depot
                return path + [start] # Returning path with return to depot
            else:
        for neighbour in bottleneck_graph[city]:
            if neighbour not in visited:
                new_visited = visited.copy()
                new_visited.add(neighbour)
                paths.append((neighbour, path + [neighbour], new_visited))
    return None

# Given cities and coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39),
}

# Calculate pairwise distances and sort edges
edges = []
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            dist = euclidean_distance(cities[i], cities[j])
            if (i, j) not in distances or distances[(i, j)] > dist:  # Take minimum distance
                distances[(i, j)] = distances[(j, i)] = dist
            edges.append((dist, i, j))
edges.sort()

# Attempt to find a tour minimizing the maximum bottleneck distance
all_nodes = list(cities.keys())
for max_weight, u, v in edges:
    # Create bottleneck graph with current max weight
    bottleneck_graph = {node: [] for node in all_nodes}
    for dist, i, j in edges:
        if dist <= max_weight:
            bottleneck_graph[i].append(j)
            bottleneck_graph[j].append(i)
    
    # Use DFS-based path finder at depot start
    tour = find_hamiltonian_path(bottleneck_graph, 0, all_nodes)
    if tour:
        total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
        max_dist = max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
        print(f"Tour: {tour}")
        print(f"Total travel cost: {total_cost}")
        print(f"Maximum distance between consecutive cities: {max_dist}")
        break