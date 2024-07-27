import math
import heapq
from collections import defaultdict, deque

# City coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Euclidean distance calculation function
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Creating a complete graph with distances as edges
n = len(coordinates)
edges = []

for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(coordinates[i], coordinates[j])
        edges.append((dist, i, j))

# Kruskal's algorithm to form a Minimum Spanning Tree (MST)
def kruskal(edges, num_nodes):
    parent = list(range(num_nodes))
    rank = [0] * num_nodes

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
    
    mst_edges = []
    edges.sort()
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, weight))
    
    return mst_edges

# Construct the MST
mst_edges = kruskal(edges, n)

# Create adjacency list of the MST
mst_adj = defaultdict(list)
for u, v, w in mst_edges:
    mst_adj[u].append((v, w))
    mst_adj[v].append((u, w))

# DFS to find the Hamiltonian path (not necessarily optimal)
def dfs(mst_adj, start):
    tour = []
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        tour.append(node)
        for neighbor, _ in reversed(mst_adj[node]):
            if neighbor not in visited:
                stack.append(neighbor)
    
    tour.append(start)  # return to the start to complete the circuit
    return tour

# Get the tour using DFS
tour = dfs(mst_adj, 0)

# Calculate the total travel cost and maximum distance between consecutive cities
total_travel_cost = 0
max_distance = 0

for i in range(1, len(tour)):
    dist = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    total_travel_cost += dist
    if dist > max_distance:
        max_distance = dist

# Outputs
print("Tour:", tour)
print("Total travel cost:", total_travel not))))travel_cost))
print("Maximum distance between consecutive cities:", max_distance)