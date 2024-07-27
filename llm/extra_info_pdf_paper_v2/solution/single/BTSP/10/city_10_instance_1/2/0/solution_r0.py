import math
from collections import defaultdict
from heapq import heappush, heappop

# City coordinates
cities = [
    (53, 68),  # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# Function to calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Build a complete graph with the distances as edge weights
def construct_graph(cities):
    n = len(cities)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((distance(cities[i], cities[j]), i, j))
    return edges, n

# Find Minimum Spanning Tree using Kruskal's Algorithm
def kruskal_mst(edges, n):
    parent = list(range(n))
    rank = [0] * n

    # Find with path compression
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    # Union by rank
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

    edges.sort()
    mst = []
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((weight, u, v))
    return mst

# Generate the Hamiltonian cycle using MST shortcuts and Eulerian Extensions
def shortcut_mst(mst, n):
    adj = defaultdict(list)
    for weight, u, v in mst:
        adj[u].append(v)
        adj[v].append(u)
    
    # Generate Euler Tour from the MST
    def euler_tour(node, visited, cycle):
        stack = [node]
        while stack:
            v = stack[-1]
            if adj[v]:
                u = adj[v].pop()
                if u in adj[v]:
                    adj[u].remove(v)  # Remove the visited edge
                    stack.append(u)
            else:
                stack.pop()
                cycle.append(v)
    
    visited = [False] * n
    cycle = []
    euler_tour(0, visited, cycle)

    # Shorten the Euler tour to Hamiltonian by skipping visited nodes
    visited = set()
    hamiltonian = []
    for node in cycle:
        if node not in visited:
            hamiltonian.append(node)
            visited.add(node)
    
    hamiltonian.append(hamiltonian[0])  # To make it a cycle starting and ending at the depot
    
    return hamiltonian

edges, num_cities = construct_graph(cities)
mst = kruskal_mst(edges, num_cities)
tour = shortcut_mst(mst, num_cities)

# Calculate total travel cost and max distance between consecutive cities
max_dist = 0
total_cost = 0
for i in range(len(tour) - 1):
    d = distance(cities[tour[i]], cities[tour[i + 1]])
    total_cost += d
    max_dist = max(max_dist, d)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")