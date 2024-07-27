import math
from itertools import permutations

# Given coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate all pair distances
distances = {}
edges = []
for i in cities.keys():
    for j in cities.keys():
        if i != j:
            dist = euclidean_distance(cities[i], cities[j])
            distances[(i, j)] = dist
            edges.append((dist, i, j))

# Sort edges based on distance
edges.sort()

def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def bottleneck_hamiltonian_path():
    for weight, u, v in edges:
        # Initialize Union-Find
        parent = list(range(len(cities)))
        rank = [0] * len(cities)
        
        # Try to create graph with edges of current weight or less
        edges_included = []
        for d, i, j in edges:
            if d <= weight:
                edges_included.append((i, j))
        
        # Use union-find to check if the graph can be hamiltonian path
        for i, j in edges_included:
            if find(parent, i) != find(parent, j):
                union(parent, rank, i, j)
        
        # Check if all nodes are connected
        root = find(parent, 0)
        if all(find(parent, i) == root for i in range(1, len(cities))):
            # Check if it is a valid path with exactly 19 edges
            if len(edges_included) == len(cities):
                return weight, edges_included

    return None, None

# Find the bottleneck hamiltonian path
max_edge_weight, edges_used = bottleneck_hamiltonian_path()

if edges_used is not None:
    # Convert edge list to ordered tour using a simple DFS
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for i, j in edges_used:
        graph[i].append(j)
        graph[j].append(i)

    # Perform DFS to get the path
    def dfs(node, visited, path):
        visited.add(node)
        path.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, path)

    visited = set()
    path = []
    dfs(0, visited, path)
    path.append(0)  # Return to the start

    # Calculate the total cost of the tour
    total_cost = sum(distances[(path[i], path[i+1])] for i in range(len(path)-1))
    max_distance = max(distances[(path[i], path[i+1])] for i in range(len(path)-1))

    print("Tour:", path)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("Failed to find a solution")