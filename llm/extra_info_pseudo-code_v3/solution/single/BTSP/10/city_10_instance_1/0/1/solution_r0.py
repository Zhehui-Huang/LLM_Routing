import math
from itertools import permutations

import networkx as nx

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def is_hamiltonian_path(graph, path, start_node):
    if path[0] != start_node or path[-1] != start_node:
        return False
    visited = set(path)
    if len(visited) != len(graph.nodes):
        return False
    for i in range(len(path) - 1):
        if path[i + 1] not in graph[path[i]]:
            return False
    return True

def solve_btsp(cities):
    num_cities = len(cities)
    edges = []
    coordinates = {i: city for i, city in enumerate(cities)}

    # Calculate all pairwise distances
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            edges.append((i, j, dist))
            edges.append((j, i, dist))

    # Sort the edge list
    edges.sort(key=lambda x: x[2])

    # Try to find Hamiltonian cycle or path with minimal bottleneck
    for threshold in edges:
        graph = nx.Graph()
        graph.add_nodes_from(coordinates.keys())
        for e in edges:
            if e[2] > threshold[2]:
                break
            graph.add_edge(e[0], e[1], weight=e[2])

        # Check all permutations to find a Hamiltonian cycle
        for perm in permutations(range(1, num_cities)):
            path = [0] + list(perm) + [0]
            if is_hamiltonian_path(graph, path, 0):
                # Calculate maximum distance in tour and total cost
                max_dist = max(euclidean_distance(coordinates[path[i]], coordinates[path[i + 1]]) for i in range(len(path) - 1))
                total_distance = sum(euclidean_distance(coordinates[path[i]], coordinates[path[i + 1]]) for i in range(len(path) - 1))
                return {
                    'Tour': path,
                    'Total travel cost': total_distance,
                    'Maximum distance between consecutive cities': max_dist
                }
    return None

# Define cities
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63),
          (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Solve the Bottleneck Traveling Salesman Problem
result = solve_btsp(cities)

print(result)