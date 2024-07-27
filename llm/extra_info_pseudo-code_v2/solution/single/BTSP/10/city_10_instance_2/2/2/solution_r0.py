import math
from itertools import permutations

# Calculate the Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_biconnected(graph, V):
    # Using depth-first search (DFS) to check if the graph is biconnected
    # Here, 'graph' is represented as an edge list, and 'V' is the number of vertices
    # For simplicity in this example, we'll just perform a biconnectivity check by ensuring all nodes are visited
    start_vertex = 0
    visited = [False] * V
    count = [0]  # Count of visited vertices in DFS
    
    def dfs(v, parent, visited, disc, low, adj):
        children = 0
        visited[v] = True
        disc[v] = low[v] = count[0]
        count[0] += 1

        for (to, _) in adj[v]:
            if not visited[to]:
                parent[to] = v
                children += 1
                success = dfs(to, parent, visited, disc, low, adj)
                
                low[v] = min(low[v], low[to])
                
                if parent[v] is None and children > 1:
                    return False
                if parent[v] is not None and low[to] >= disc[v]:
                    return False
            elif to != parent[v]:
                low[v] = min(low[v], disc[to])
        
        return True
    
    # Construct adjacency list for undirected graph
    adj = [[] for _ in range(V)]
    for u, v in graph:
        adj[u].append((v, 0))
        adj[v].append((u, 0))
    
    disc = [-1] * V
    low = [-1] * V
    parent = [None] * V
    
    if not dfs(start_vertex, parent, visited, disc, low, adj):
        return False
    
    return all(visited)

# Create the initial weighted complete graph
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54),
          (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]
num_cities = len(cities)

# Step 0: Initialize the solution set E_BB as an empty set
edges = [(i, j, distance(cities[i], cities[j])) for i in range(num_cities) for j in range(i+1, num_cities)]
edges.sort(key=lambda x: x[2])  # Sort edges in non-decreasing order of their weights

E_BB = []
added_edges = set()

# Step 1: Augmentation
for edge in edges:
    E_BB.append((edge[0], edge[1]))
    added_edges.add((edge[0], edge[1]))
    added_edges.add((edge[1], edge[0]))
    
    # Step 2: Check biconnected condition
    if is_biconnected(list(added_edges), num_cities):
        max_distance = edge[2]
        break

# Step 2: Tour Identification
# Generating permutations of vertex indices {1, ..., n-1}, since 0 is the depot
perms = permutations(range(1, num_ciles))
best_tour = None
best_max_distance = float('inf')

for perm in perms:
    tour = [0] + list(perm) + [0]
    tour_distance = 0
    max_leg_dist = 0
    
    for i in range(len(tour)-1):
        dist = distance(cities[tour[i]], cities[tour[i+1]])
        tour_distance += dist
        max_leg_dist = max(max_leg_dist, dist)
        
    if max_leg_dist < best_max_distance:
        best_max_distance = max_leg_dist
        best_tour = tour

# Output Results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {tour_distance}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")