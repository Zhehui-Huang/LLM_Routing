import itertools
import math
from scipy.spatial.distance import euclidean

# Define the cities with coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate distance
def calculate_distance(city1, city2):
    return euclidean(city1, city2)

# List of edges with distances
edges = []
for i in range(len(cities)):
    for j in range(i+1, len(cities)):
        dist = calculate_distance(cities[i], cities[j])
        edges.append((dist, i, j))

# Sort edges by distance
edges.sort()

# Find hammiltonian path using a DFS approach
def is_hamiltonian_path_feasible(vertex, visited, adj_map):
    if len(visited) == len(cities) and 0 in adj_map[vertex]:
        return True
    return False

def dfs(current, visited, adj_map, path, max_edge_distance):
    if is_hamiltonian_path_feasible(current, visited, adj_map):
        path.append(0)
        return True, path, max_edge_distance
    for neighbor in adj_map[current]:
        if neighbor not in visited or (neighbor == 0 and len(visited) == len(cities)):
            path.append(neighbor)
            visited.add(neighbor)
            edge_dist = calculate_distance(cities[current], cities[neighbor])
            result, res_path, res_max_dist = dfs(neighbor, visited, adj_map, path, max(max_edge_distance, edge_dist))
            if result:
                return True, res_path, res_max_dist
            path.pop()
            visited.remove(neighbor)
    return False, path, max_edge_distance

# Iterating through increasing bottleneck thresholds
for max_dist, _, _ in edges:
    # Build adjacency map with current max_dist
    adj_map = {i: set() for i in range(len(cities))}
    for dist, u, v in edges:
        if dist <= max_dist:
            adj_map[u].add(v)
            adj_map[v].add(u)
        else:
            break

    path = [0]
    visited = {0}
    result, path, max_path_distance = dfs(0, visited, adj_map, path, 0)
    if result:
        total_distance = sum(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1))
        print(f"Tour: {path}")
        print(f"Total travel cost: {total_distance}")
        print(f"Maximum distance between consecutive cities: {max_path_distance}")
        break