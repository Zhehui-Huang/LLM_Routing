import math
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
for i in cities:
    for j in cities:
        if i < j:
            distance = calc_distance(i, j)
            edges.append((distance, i, j))

edges.sort()  # Sort edges based on distances

# Use Kruskal's algorithm to build MST and then check for Hamiltonian cycle with DFS
def has_hamiltonian_cycle(limit, return_cycle=False):
    # Create subgraph with edges not exceeding the limit
    parent = list(range(len(cities)))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX
    
    mst_edges = []
    for dist, u, v in edges:
        if dist > limit:
            break
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v))
    
    # Check if connected
    if len(mst_edges) != len(cities) - 1:
        return False
    
    # Trying to find a Hamiltonian cycle in the MST
    adj = {i: [] for i in cities}
    for u, v in mst_edges:
        adj[u].append(v)
        adj[v].append(u)
    
    cycle = []
    visited = [False] * len(cities)
    def dfs(node):
        cycle.append(node)
        visited[node] = True
        if len(cycle) == len(cities) and cycle[0] in adj[cycle[-1]]:
            return True
        for next_node in adj[node]:
            if not visited[next_node]:
                if dfs(next_node):
                    return True
        cycle.pop()
        visited[node] = False
        return False
    
    # Start DFS from node 0 (depot city)
    if dfs(0):
        if return_cycle:
            cycle.append(cycle[0])  # complete the cycle back to the start point
            return cycle
        return True
    return False

def find_bottleneck_tsp():
    low, high = 0, max(dist for dist, _, _ in edges)
    best_dist = None
    
    while low <= high:
        mid = (low + high) // 2
        if has_hamiltonian_cycle(mid):
            best_dist = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return best_dist, has_hamiltonian_cycle(best_dist, return_cycle=True)

best_weight, route = find_bottleneck_tsp()

def calculate_metrics(route):
    max_dist = 0
    total_dist = 0
    for i in range(1, len(route)):
        dist = calc_distance(route[i - 1], route[i])
        total_dist += dist
        max_dist = max(max_dist, dist)
    return route, total_dist, max_dist

final_route, final_total_dist, final_max_dist = calculate_metrics(route)

print(f"Tour: {final_route}")
print(f"Total travel cost: {final_total_dist}")
print(f"Maximum distance between consecutive cities: {final_max_dist}")