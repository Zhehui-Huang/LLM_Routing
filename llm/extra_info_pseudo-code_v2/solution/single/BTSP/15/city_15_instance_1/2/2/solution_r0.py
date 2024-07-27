import numpy as np
import sys
from scipy.sparse import csgraph

# Cities coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate Euclidean distances
def calculate_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create distance matrix
n = len(coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Algorithm BB to find bottleneck-optimal biconnected subgraph
def find_biconnected_subgraph(distance_matrix):
    n = len(distance_matrix)
    edges = [(i, j, distance_matrix[i][j]) for i in range(n) for j in range(i + 1, n)]
    edges.sort(key=lambda x: x[2])  # Sort based on distance

    # Union-Find for cycle detection
    parent = list(range(n))

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            parent[root2] = root1

    # Initialize empty graph for edges in biconnected subgraph
    biconn_graph = np.zeros_like(distance_matrix)

    # Kruskal-like mechanism to avoid disconnected graph
    for u, v, cost in edges:
        if find(u) != find(v):
            biconn_graph[u][v] = biconn_graph[v][u] = cost
            union(u, v)

    # Check connectivity
    if len(set(find(x) for x in range(n))) != 1:
        print("Graph is not connected")

    return biconn_graph

# Approximate tour through Hamiltonian cycle finding in the squared graph (using MST for simplicity)
def approximate_btsp_tour(biconn_graph):
    mst = csgraph.minimum_spanning_tree(biconn_graph)
    mst = mst.toarray().astype(float)  # Convert to dense format
    np.fill_diagonal(mst, 0)
    
    # Double tree traversal
    tour = [0]
    visited = set(tour)

    def dfs(v):
        for u in range(len(mst)):
            if mst[v][u] != 0 and u not in visited:
                visited.add(u)
                tour.append(u)
                dfs(u)
                tour.append(v)

    dfs(0)
    tour.append(0)  # complete the tour back to the depot

    return tour

# Find the tour and evaluate its cost and bottleneck
def evaluate_tour(tour, distance_matrix):
    max_distance = 0
    total_cost = 0
    for i in range(1, len(torial)):
        d = distance_matrix[tour[i-1]][tour[i]]
        total_cost += d
        if d > max_distance:
            max_distance = d
    return tour, total_cost, max_distance

# Processing the tour
biconn_graph = find_biconnected_subgraph(distance_matrix)
tour = approximate_btsp_tour(biconn_graph)
tour, total_cost, max_distance = evaluate_tour(tour, distance_matrix)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)