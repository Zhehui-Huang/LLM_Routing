import math
from queue import PriorityQueue

# Define the cities coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

n = len(cities)

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate all pairwise distances
edges = []
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(cities[i], cities[j])
        edges.append((dist, i, j))

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

# Kruskal's algorithm to find Minimum Spanning Tree (MST)
def kruskal(edges, n):
    edges.sort()
    parent = []
    rank = []
    
    for node in range(n):
        parent.append(node)
        rank.append(0)
    
    mst = []
    
    for edge in edges:
        weight, u, v = edge
        
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, weight))
    
    return mst

# Generate MST
mst = kruskal(edges, n)

# Function to get the Eulerian tour from the MST
def get_eulerian_tour(mst, start):
    # Create the adjacency list
    adj = {i: [] for i in range(n)}
    for u, v, _ in mst:
        adj[u].append(v)
        adj[v].append(u)
    
    # Initialize variables for DFS
    stack = [start]
    path = []
    while stack:
        v = stack[-1]
        if adj[v]:
            u = adj[v].pop()
            adj[u].remove(v)
            stack.append(u)
        else:
            path.append(stack.pop())
    
    return path

# Finding the Eulerian tour for the doubled MST
tour = get_eulerian_tour(mst, 0)

# Removing repeated nodes to form a Hamiltonian cycle (shortcutting)
hamiltonian_cycle = []
visited = [False] * n
for city in tour:
    if not visited[city]:
        visited[city] = True
        hamiltonian_cycle.append(city)

# Add starting city to complete cycle
hamiltonian_cycle.append(hamiltonian_cycle[0])

# Calculate total travel cost and bottleneck distance
total_distance = 0
max_distance = 0
for i in range(len(hamiltonian_cycle) - 1):
    dist = euclidean_distance(cities[hamiltonian_cycle[i]], cities[hamiltonian_cycle[i+1]])
    total_distance += dist
    max_distance = max(max_distance, dist)

# Output results formatted as requested
print(f"Tour: {hamiltonian_cycle}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")