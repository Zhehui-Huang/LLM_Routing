import math
import itertools
from heapq import heappop, heappush

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate pairwise distances
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Find MST using Kruskal's algorithm
def kruskal():
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            heappush(edges, (distances[i][j], i, j))
    
    parent = list(range(n))
    rank = [0] * n

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(r1, r2):
        if rank[r1] > rank[r2]:
            parent[r2] = r1
        elif rank[r1] < rank[r2]:
            parent[r1] = r2
        else:
            parent[r2] = r1
            rank[r1] += 1

    mst = []
    while edges and len(mst) < n - 1:
        weight, u, v = heappop(edges)
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            union(root_u, root_v)
            mst.append((u, v, weight))
    return mst

mst = kruskal()

# Create an adjacency list for the MST
adj_list = [[] for _ in range(n)]
for u, v, _ in mst:
    adj_list[u].append(v)
    adj_list[v].append(u)

# DFS to get the Hamiltonian path
def dfs(curnode, visited, path):
    visited.add(curnode)
    path.append(curnode)
    for neighbor in adj_list[curnode]:
        if neighbor not in visited:
            dfs(neighbor, visited, path)

visited = set()
path = []
dfs(0, visited, path)
path.append(0)  # complete the cycle by returning to the depot

# Calculate total cost and max distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(1, len(path)):
    dist = distances[path[i-1]][path[i]]
    total_cost += dist
    max_distance = max(max_distance, dist)

tour_output = {
    "Tour": path,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

print(tour_output)