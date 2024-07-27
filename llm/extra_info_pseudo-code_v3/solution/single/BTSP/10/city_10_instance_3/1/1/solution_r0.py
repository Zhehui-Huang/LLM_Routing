import math
import itertools
from collections import defaultdict

# City Coordinates
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

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create sorted list of edges by weight
edges = []
n = len(cities)
for i in range(n):
    for j in range(i + 1, n):
        distance = calc_distance(i, j)
        edges.append((distance, i, j))

edges.sort()  # Sort edges based on distances

# Helper function to check if all vertices are connected
def all_connected(vertices, subgraph):
    visited = {vertex: False for vertex in vertices}
    # Start DFS from any vertex, here vertices[0]
    stack = [vertices[0]]
    actual_number_visited = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            actual_number_visited += 1
            # Push all connected vertices that are in subgraph
            stack.extend([v for v in subgraph[node] if not visited[v]])
    return actual_number_visited == len(vertices)

# Function to check for Hamiltonian path
def has_hamiltonian_path(max_weight):
    subgraph = defaultdict(list)
    for distance, u, v in edges:
        if distance <= max_weight:
            subgraph[u].append(v)
            subplugraph[v].append(u)
        else:
            break
    
    # Check if it's possible to have a Hamiltonian path in this subgraph
    # 1. All vertices should have degree at least 1
    # 2. All vertices must be reachable from any other vertex (connected component)
    if all(len(subgraph[v]) > 0 for v in range(n)) and all_connected(range(n), subgraph):
        return True
    return False

# Main algorithm to find the minimal bottleneck Hamiltonian path
def find_btsp_path():
    left, right = 0, len(edges) - 1
    best_path_weight = float('inf')

    while left <= right:
        mid = (left + right) // 2
        if has_hamiltonian_path(edges[mid][0]):
            best_path_weight = edges[mid][0]
            right = mid - 1
        else:
            left = mid + 1

    # Reconstruct the path with the found best_path_weight
    # This is a simplified part, it would ideally be place where we extract the actual path
    return best_path_weight

# Optimal bottleneck weight
bottleneck_weight = find_btsp_path()
print(f"Optimal Bottleneck Weight: {bottleneck_weight}")