import math
from itertools import permutations

# Given city coordinates with depots and others
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate all pairs and calculate Euclidean distances
all_edges = [(i, j, euclidean_distance(cities[i], cities[j])) for i in range(len(cities)) for j in range(i + 1, len(cities))]

# Sort edges by distance
sorted_edges = sorted(all_edges, key=lambda x: x[2])

# Find the minimum bottleneck tree using a union-find to help ensure connectivity
parent = list(range(len(cities)))
rank = [0] * len(cities)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

# Create the graph using edges until it's fully connected
mst = []
for u, v, w in sorted_edges:
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, w))

# Simply finding a hamiltonian path brute-force from the constructed MST
def find_tour(mst):
    # Create adjacency list
    adj = {i: [] for i in range(len(cities))}
    for u, v, w in mst:
        adj[u].append(v)
        adj[v].append(u)
    
    # Use a simple DFS to find Hamiltonian path
    visited = [False] * len(cities)
    path = []

    def dfs(v):
        visited[v] = True
        path.append(v)
        if len(path) == len(cities):
            return True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
        path.pop()
        visited[v] = False
        return False
    
    for start in range(len(cities)):  # Try all possible starting points
        if dfs(start):
            break

    # Close the tour by returning to the starting node
    if path[0] != 0:  # Ensure tour starts and ends at city 0
        # Rotate path to start at 0
        zero_index = path.index(0)
        path = path[zero My_listinsert(0, path.pop())] + path[:zero_index]
    path.append(path[0])  # Make it a round trip
    return path, mst

tour, used_edges = find_tour(mst)

# Calculate tour cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Display the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))