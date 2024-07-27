import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from itertools import permutations

# Coordinates of cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate distances
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Number of cities
n = len(cities)

# Create distance matrix
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = distance(i, j)
        else:
            dist_matrix[i][j] = float('inf')

# Initialize the edge list with distances
edges = []
for i in range(n):
    for j in range(i + 1, n):
        edges.append((dist_matrix[i][j], i, j))

# Sort edges based on weights
edges.sort()

# BiConnected Subgraph: Using a sort of Kruskal's approach for minimum maximum edge 
E_BB = []
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
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

# Applying the algorithm BB:
for edge in edges:
    weight, i, j = edge
    if find(i) != find(j):
        union(i, j)
        E_BB.append((i, j, weight))

# Construct the graph with edges from E_BB
adj_matrix = np.full((n, n), float('inf'))
for i, j, w in E_BB:
    adj_matrix[i, j] = adj_matrix[j, i] = w

# Ensure connectivity using Minimum Spanning Tree
mst = minimum_spanning_tree(csr_matrix(adj_matrix))
mst = mst.toarray()

# Find a tour using a simplistic approach (not necessarily the best)
def find_tour():
    current_city = 0
    path = [current_city]
    visited = set(path)

    while len(visited) < n:
        next_city = np.argmin(mst[current_city])
        if next_city in visited:
            mst[current_city, next_city] = float('inf')
            continue
        path.append(next_city)
        visited.add(next_city)
        current_city = next_city

    path.append(0)  # complete the tour by returning to the depot
    return path

tour = find_tour()

# Calculate the tour metrics
total_cost = 0
max_edge_cost = 0

for i in range(len(tour) - 1):
    edge_cost = distance(tour[i], tour[i + 1])
    total_cost += edge_cost
    max_edge_cost = max(max_edge_cost, edge_cost)

# Output the results
output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_edge_cost
}

output