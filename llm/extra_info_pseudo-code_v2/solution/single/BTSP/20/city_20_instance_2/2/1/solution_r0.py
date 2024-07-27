import numpy as np
import math
from itertools import permutations

# Define cities' coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), 
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
    (51, 58), (30, 48)
]

num_cities = len(cities)

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Construct the distance matrix
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = distance(cities[i], cities[j])

# Step 1: Bottleneck-optimal Biconnected Subgraph
def minimal_bottleneck_biconnected_subgraph():
    edges = []
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            edges.append((dist_matrix[i][j], i, j))
    
    # Sort by weights
    edges.sort()

    # Kruskal-like process to create a biconnected subgraph
    parent = list(range(num_cities))
    rank = [0] * num_cities
    
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

    mst_edges = []
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v))

    # Check connectivity
    if len(mst_edges) != num_cities - 1:
        return None
    return mst_edges

# Step 2: Identify Tour
def identify_tour(edges):
    # Use a simple method to convert the tree to a tour by visiting vertices in a DFS manner
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * num_cities
    tour = []

    def dfs(v):
        visited[v] = True
        tour.append(v)
        for next in graph[v]:
            if not visited[next]:
                dfs(next)

    # Start DFS from the depot (city 0)
    dfs(0)
    # Make it a round trip by returning to the starting node
    tour.append(0)
    
    return tour

# Get the edges from the minimal spanning tree that should form a biconnected subgraph
mbb_edges = minimal_bottleneck_biconnected_subgraph()

# Calculate the total travel cost and maximum edge cost in the tour
if mbb_edges:
    tour = identify_tour(mbb_edges)
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = dist_matrix[tour[i-1]][tour[i]]
        total_cost += dist
        max_distance = max(max_distance, dist)
    
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("Failed to find a valid biconnected subgraph")