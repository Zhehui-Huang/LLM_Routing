import math
import itertools

# Definition of city coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# Define the function for computing Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Generate all edges with distance in a complete graph
def create_graph(cities):
    edges = {}
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            dist = euclidean_distance(cities[i], cities[j])
            edges[(i, j)] = dist
            edges[(j, i)] = dist
    return edges

# Computing an approximate BTSP tour
def btsp_tour(cities):
    n = len(cities)
    graph = create_graph(cities)
    all_edges = sorted(graph.items(), key=lambda item: item[1])
    
    # Finding minimal spanning tree using Kruskal's algorithm
    parent = list(range(n))
    rank = [0] * n

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

    mst = []
    for (u, v), d in all_edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, d))
    
    # Construct the tour from MST
    adj = {i: [] for i in range(n)}
    for u, v, d in mst:
        adj[u].append((v, d))
        adj[v].append((u, d))

    # Find euler tour using Hierholzer's algorithm in MST
    def find_euler_tour(node):
        euler = []
        stack = [node]
        while stack:
            u = stack[-1]
            if adj[u]:
                v, _ = adj[u].pop()
                stack.append(v)
            else:
                euler.append(stack.pop())
        return euler

    euler_tour = find_euler_tour(0)
    
    # Make the tour Hamiltonian by removing repeated nodes (shortcutting)
    visited = set()
    hamiltonian_tour = []
    for node in euler_tour:
        if node not in visited:
            visited.add(node)
            hamiltonian_tour.append(node)
    
    # Ensure the tour ends at the starting point
    hamiltonian_tour.append(hamiltonian_tour[0])
    
    # Calculate tour cost and max distance between consecutive cities
    total_cost = sum(graph[(hamiltonian_tour[i], hamiltonian_tour[i+1])] for i in range(len(hamiltonian_tour) - 1))
    max_distance = max(graph[(hamiltonian_tour[i], hamiltonian_tour[i+1])] for i in range(len(hamiltonian_tour) - 1))

    return hamiltonian_tour, total_cost, max_distance

# Perform the BTSP tour calculation
tour, total_cost, max_distance = btsp_tour(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")