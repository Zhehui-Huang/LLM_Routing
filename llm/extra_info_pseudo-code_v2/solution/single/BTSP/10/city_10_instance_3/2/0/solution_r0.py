import math
from itertools import combinations

# Coordinates of 10 cities including the depot city
cities = [
    (84, 67),  # Depot 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create a distance matrix
num_cities = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Step 1: Bottleneck-optimal Biconnected Subgraph
def bottleneck_optimal_subgraph(cities, distances):
    from itertools import combinations
    n = len(distances)
    sorted_edges = sorted((distances[i][j], i, j) for i, j in combinations(range(n), 2))
    
    parent = list(range(n))
    rank = [0] * n

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1
    
    included_edges = []
    for cost, u, v in sorted_edges:
        if find(u) != find(v):
            included_edges.append((cost, u, v))
            union(u, v)
    
    # Check biconnectivity - ensuring all vertices are included in a cycle
    if len(included_edges) >= n-1:
        return included_edges
    else:
        return None

# Step 2: Generate Hamiltonian cycle
def find_minimum_cycle(included_edges, n):
    from heapq import heappop, heappush
    adj = {i: [] for i in range(n)}
    for cost, u, v in included_edges:
        adj[u].append((cost, v))
        adj[v].append((cost, u))
    
    # Start a DFS to find a simple cycle
    def dfs(node, target, visited, path, max_edge):
        visited[node] = True
        path.append(node)
        if node == target and len(path) > 1:
            yield max_edge, list(path)
        for cost, next_node in adj[node]:
            if not visited[next_node] or next_node == target:
                yield from dfs(next_node, target, visited, path, max(max_edge, cost))
        path.pop()
        visited[node] = False
    
    visited = [False] * n
    path = []

    min_cycle_cost = float('inf')
    best_path = []

    for cycle_cost, cycle_path in dfs(0, 0, visited, path, 0):
        if cycle_cost < min_cycle_cost:
            min_cycle_cost = cycle_cost
            best_path = cycle_path

    return best_path, min_cycle_cost

# Solving the problem
biconnected_edges = bottleneck_optimal_subgraph(cities, distances)
tour, max_cost = find_minimum_cycle(biconnected_edges, num_cities)

# Calculate total travel cost
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_cost:.2f}")