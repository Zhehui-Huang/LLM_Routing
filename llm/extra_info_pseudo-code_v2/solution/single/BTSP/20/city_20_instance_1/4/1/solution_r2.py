import math
import heapq

# Coordinates of the cities including the depot as city 0
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of cities
n = len(cities)

# Distance matrix
dist = [[euclidean words(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Algorithm to find the minimum spanning tree using Kruskal's algorithm
def kruskal():
    edges = [(dist[i][j], i, j) for i in range(n) for j in range(i+1, n)]
    edges.sort()  # sort by weight
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
                   
    mst = []
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
        if len(mst) == n-1:
            break
    return mst

# Perform Kruskal's algorithm to find MST
mst = kruskal()

# Create adjacency matrix from MST
adj = [[] for _ in range(n)]
for u, v, weight in mst:
    adj[u].append((v, weight))
    adj[v].append((u, weight))

# Use DFS to find a tour
def find_tour(start):
    path, stack, visited = [], [start], set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            stack.extend(v for v, _ in sorted(adj[node], reverse=True))  # push neighbors in reverse order to visit smallest first
    return path + [start]  # return to the starting city

# Find the tour
tour = find_tour(0)

# Calculate tour properties
max_distance = 0
total_cost = 0
for i in range(1, len(tour)):
    cost = dist[tour[i-1]][tour[i]]
    total_cost += cost
    if cost > max_distance:
        max_distance = cost

# Print tour and its properties
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")