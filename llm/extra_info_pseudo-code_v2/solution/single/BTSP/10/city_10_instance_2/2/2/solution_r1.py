import math
from itertools import permutations

# Calculate the Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create the initial weighted graph from city coordinates
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), 
          (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]
num_cities = len(cities)

# Generate all pairs distance
edges = [(i, j, distance(cities[i], cities[j])) for i in range(num_cities) for j in range(i + 1, num_cities)]
edges.sort(key=lambda x: x[2])

# Function to find the root of a node
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

# Function to do union of two subsets
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

# Find MST using Kruskal's Algorithm
def kruskal(edges):
    result = []  # This will store the resultant MST
    i = 0
    e = 0
    
    parent = []
    rank = []
    
    # Create V subsets with single elements
    for node in range(num_cities):
        parent.append(node)
        rank.append(0)
    
    # Number of edges to be taken is equal to V-1
    while e < num_cities - 1:
        # Step 2: Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far.
        if i >= len(edges):
            break
        (u, v, w) = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        
        if x != y:
            e = e + 1
            result.append((u, v))
            union(parent, rank, x, y)
    return result

mst_edges = kruskal(edges)

# Hamiltonian cycle: as the MST does not have repeated vertices, we'll do a DFS for simplicity in an undirected cycle
def dfs(v, visited, adj, path):
    visited[v] = True
    path.append(v)
    
    for i in adj[v]:
        if not visited[i]:
            dfs(i, visited, adj, path)

adj_list = [[] for _ in range(num_cities)]
for u, v in mst_edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

# Starting DFS from depot i.e., node 0
visited = [False] * num_cities
tour = []
dfs(0, visited, adj_list, tour)
tour.append(0)  # returning to the depot

# Calculate total cost and maximum edge in the tour
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    dist = distance(cities[tour[i]], cities[tour[i + 1]])
    total_cost += dist
    max_distance = max(max_distance, dist)

# Outputs
print("Tour: ", tour)
print("Total travel cost: ", total_cost)
print("Maximum distance between consecutive cities: ", max_distance)