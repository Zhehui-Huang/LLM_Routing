import itertools
import math
from collections import defaultdict

# City coordinates
cities = {
    0: (53, 68), 
    1: (75, 11), 
    2: (91, 95), 
    3: (22, 80), 
    4: (18, 63), 
    5: (54, 91), 
    6: (70, 14), 
    7: (97, 44), 
    8: (17, 69), 
    9: (95, 89)
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create a list of all edges with distances
edges = []
for city1 in cities:
    for city2 in cities:
        if city1 != city2:
            edges.append((city1, city2, euclidean_distance(city1, city2)))

# Sort edges based on weight
edges.sort(key=lambda x: x[2])

# Helper function to check if a Hamiltonian cycle that meets the distance constraint exists
def hamiltonian_path_exists(max_distance):
    def dfs(node, visited, path):
        if len(visited) == len(cities):
            return path + [(0, )]
        
        for neighbor in graph[node]:
            if neighbor not in visited and distances[(min(node, neighbor), max(node, neighbor))] <= max_distance:
                new_path = dfs(neighbor, visited | {neighbor}, path + [(neighbor, )])
                if new_path:
                    return new_path
        return None
    
    graph = defaultdict(list)
    distances = {}
    
    for city1, city2, distance in edges:
        if distance <= max_distance:
            graph[city1].append(city2)
            graph[city2].append(city1)
            distances[(min(city1, city2), max(city1, city2))] = distance
    
    # Start DFS from node 0
    path = dfs(0, {0}, [(0,)])
    return path

# Main algorithm to find the minimum bottleneck Hamiltonian cycle
for max_distance in (edge[2] for edge in edges):
    path = hamiltonian_path_exists(max_distance)
    if path:
        total_distance = sum(euclidean_distance(path[i][0], path[(i + 1) % len(path)][0]) for i in range(len(path)))
        max_edge_distance = max(euclidean_date_distance(path[i][0], path[(i + 1) % len(path)][0]) for i in range(len(path)))
        path_indices = [city[0] for city in path]
        break

print("Tour:", path_indices)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_edge_distance)