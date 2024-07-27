import itertools
import math
from sys import maxsize

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p20)** 2 + (p1[1] - p2[1]) ** 2)

cities = [
    (16, 90), # Depot city
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

def create_sorted_edges(cities):
    num_cities = len(cities)
    edges = []
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            if i != j:
                dist = euclidean_distance(cities[i], cities[j])
                edges.append((dist, i, j))
    edges.sort()
    return edges

def create_bottleneck_graph(cities, threshold):
    num_cities = len(cities)
    graph = {i: [] for i in range(num_cities)}
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j and euclidean_distance(cities[i], cities[j]) <= threshold:
                graph[i].append(j)
    return graph

def has_hamiltonian_path(graph, start_node):
    # Checking Hamiltonian path using backtracking approach, for simplicity.
    n = len(graph)
    path = []
    
    def backtrack(current, visited):
        nonlocal path
        if len(path) == n:
            return True
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                if backtrack(neighbor, visited):
                    return True
                visited.remove(neighbor)
                path.pop()
        return False

    visited = {start_node}
    path = [start_node]
    if backtrack(start_node, visited):
        return True, path
    return False, []

def find_btsp_tour(cities):
    edges = create_sorted_edges(cities)
    for dist, _, _ in edges:
        graph = create_bottleneck_graph(cities, dist)
        has_path, path = has_hamiltonian_path(graph, 0)
        if has_path and len(path) == len(cities):
            path.append(0) # To make it round-trip
            max_dist = dist
            total_cost = sum(euclidean_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path) - 1))
            return path, total_cost, max_dist
    return None

tour, total_cost, max_consecutive_dist = find_btsp_tour(cities)
print("Tour:", tour)
print("Total travel cost:", int(total_cost))
print("Maximum distance between consecutive cities:", int(max_consecutive_dist))