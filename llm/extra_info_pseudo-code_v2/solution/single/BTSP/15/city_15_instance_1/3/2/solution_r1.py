import numpy as np
from heapq import heappop, heappush
from collections import defaultdict

# Define the cities and their coordinates
city_locations = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Number of cities
n = len(city_locations)

# Calculate the Euclidean distances between each pair of cities
def calculate_distance(city1, city2):
    x1, y1 = city_locations[city1]
    x2, y2 = city_blocks[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create distance matrix
distance_matrix = [[calculate_distance(i, j) for j in range(n)] for i in range(n)]

# Functions to find the union and find actions of the Union-Find data structure
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent, parent[i])
        return parent[i]

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

def construct_mst():
    edges = [(distance_matrix[i][j], i, j) for i in range(n) for j in range(i + 1, n)]
    edges.sort()
    
    parent = list(range(n))
    rank = [0] * n
    mst = []
    
    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, weight))
            union(parent, rank, u, v)
            if len(mst) == n - 1:
                break
    return mst

# Function to construct the tour using a greedy strategy from the MST
def construct_tour(mst):
    # Build the graph from MST
    adj = defaultdict(list)
    for u, v, w in mst:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Use a DFS to find a Hamiltonian path (not necessarily minimal)
    start = 0
    tour = []
    visited = set()
    
    def dfs(node):
        visited.add(node)
        tour.append(node)
        for neighbor, _ in sorted(adj[node], key=lambda x: x[1]):  # sort neighbors by weight
            if neighbor not in visited:
                dfs(neighbor)
                
    dfs(start)
    tour.append(start)  # complete the cycle

    return tour

# Perform calculations
mst = construct_mst()
tour = construct_tour(mst)

# Calculate costs: total cost and maximum leg distance
total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_leg_distance = max(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_distance)