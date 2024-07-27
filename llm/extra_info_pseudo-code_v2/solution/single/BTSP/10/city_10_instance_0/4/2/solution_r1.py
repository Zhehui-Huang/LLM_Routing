import numpy as np

# Define city coordinates
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

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create a distance matrix
n = len(cities)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i, j] = distance(i, j)

# Create graph with city indices and corresponding distances
edges = [(dist_matrix[i, j], i, j) for i in range(n) for j in range(n) if i < j]
edges.sort()  # Sort edges based on distance

# Kruskal's-like method to find a subset of edges forming a biconnected graph
parent = list(range(n))
rank = [0] * n

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

# Generate minimum spanning tree
mst = []
for weight, u, v in edges:
    if find(parent, u) != find(parent, v):
        mst.append((u, v, weight))
        union(parent, rank, u, v)

# Use MST to form a tour starting and ending at the depot
from collections import defaultdict

graph = defaultdict(list)
for u, v, w in mst:
    graph[u].append(v)
    graph[v].append(u)

# Find a Eulerian tour using Hierholzer's Algorithm
def find_eulerian_tour(graph, start):
    stack = [start]
    path = []
    while stack:
        vertex = stack[-1]
        if graph[vertex]:
            next_vertex = graph[vertex].pop()
            # Remove the reverse edge
            graph[nextust_vertex].remove(vertex)
            stack.append(next_vertex)
        else:
            path.append(stack.pop())
    return path

eulerian_tour = find_eulerian_tour(graph, 0)

# Output the tour
tour = [0]
visited = set([0])
for city in eulerian_tour:
    if city not in visited:
        tour.append(city)
        visited.add(city)

# Add depot to complete the circuit
tour.append(0)

# Calculate travel cost and maximum distance between consecutive cities
total_cost = 0
max_dist = 0
for i in range(len(tour)-1):
    cost = distance(tour[i], tour[i+1])
    total_cost += cost
    max_dist = max(max_dist, cost)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)