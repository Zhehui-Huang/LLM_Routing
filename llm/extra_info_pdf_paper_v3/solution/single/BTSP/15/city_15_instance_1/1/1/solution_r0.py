import math
import heapq
from collections import defaultdict

# Coordinates of cities
coordinates = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
               (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
               (83, 96), (60, 50), (98, 1)]

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def find_parent(parent, i):
    if parent[i] == i:
        return i
    else:
        return find_parent(parent, parent[i])

def mst_kruskal(coords):
    """ Compute the MST using Kruskal's algorithm """
    edges = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            heapq.heappush(edges, (euclidean_distance(coords[i], coords[j]), i, j))
    
    parent = list(range(len(coords)))
    rank = [0] * len(coords)
    mst = defaultdict(list)

    while edges:
        weight, u, v = heapq.heappop(edges)
        root_u = find_parent(parent, u)
        root_v = find_parent(parent, v)
        
        if root_u != root_v:
            mst[u].append((v, weight))
            mst[v].append((u, weight))
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
    
    return mst

def dfs_tour(mst, start):
    """ Perform DFS to obtain a tour from the MST """
    tour = []
    visited = set()
    
    def dfs(node):
        visited.add(node)
        tour.append(node)
        for neighbor, _ in mst[node]:
            if neighbor not in visited:
                dfs(neighbor)
                tour.append(node)
    
    dfs(start)
    return tour

# Get the MST
mst = mst_kruskal(coordinates)
# Generate tour using DFS
tour = dfs_tour(mst, 0)

# Calculate the maximum distance and total cost
max_distance = 0
total_cost = 0
for i in range(1, len(tour)):
    dist = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))