import math

# City coordinates
cities = [
    (84, 67),  # Depot city 0
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

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a matrix of distances between each pair of cities
n = len(cities)
dist_matrix = [[calc_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Kruskal's algorithm to find the Minimum Spanning Tree (MST)
parent = list(range(n))
rank = [0] * n

def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]

def union(i, j):
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        if rank[root_i] > rank[root_j]:
            parent[root_j] = root_i
        else:
            parent[root_i] = root_j
            if rank[root_i] == rank[root_j]:
                rank[root_j] += 1

# List of all edges sorted by distance
edges = [(dist_matrix[i][j], i, j) for i in range(n) for j in range(i + 1, n)]
edges.sort()

# Kruskal's algorithm to construct the MST
mst = []
for dist, i, j in edges:
    if find(i) != find(j):
        union(i, j)
        mst.append((i, j))

# Find a path including all nodes using the edges in the MST
# To ensure we return to the starting node, a simplistic approach is
# to add a DFS to order nodes and then directly connect back to the start.
from collections import defaultdict, deque

graph = defaultdict(list)
for i, j in mst:
    graph[i].append(j)
    graph[j].append(i)

def dfs(node, visited):
    path = []
    stack = [node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            for neighbor in sorted(graph[node], reverse=True):
                if neighbor not in visited:
                    stack.append(neighbor)
    return path

visited = set()
tour = dfs(0, visited)
tour.append(0)  # return to the depot

# Calculating cost metrics
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_consecutive_distance = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)