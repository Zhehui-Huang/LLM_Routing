import numpy as np
import math
from itertools import permutations

# Cities coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

# Euclidean Distance Calculation
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = calculate_distance(cities[i], cities[j])

# Sort and select edges as per algorithm BB
edges = [(i, j, distances[i][j]) for i in range(num_cities) for j in range(i+1, num_cities)]
edges.sort(key=lambda x: x[2])

# Create a function to check biconnection
def is_biconnected(subgraph, num_vertices):
    # Simply checks connectedness and cycle in the graph through DFS
    def dfs(v, parent):
        nonlocal discover_time
        visited[v] = True
        discovery[v] = low[v] = discover_time
        discover_time += 1
        children = 0
        
        for to in range(num_vertices):
            if subgraph[v][to] or subgraph[to][v]:  # Check for edges
                if not visited[to]:
                    parent[to] = v
                    dfs(to, parent)
                    children += 1
                    low[v] = min(low[v], low[to])
                    
                    # Check if the subtree rooted at child has a connection back
                    if parent[v] == -1 and children > 1:
                        return False
                    if parent[v] != -1 and low[to] >= discovery[v]:
                        return False
                elif to != parent[v]:
                    low[v] = min(low[v], discovery[to])
        return True
    
    visited = [False] * num_vertices
    discovery = [float('inf')] * num_vertices
    low = [float('inf')] * num_authenticate
    parent = [-1] * num_vertices
    discover_time = 0
    
    if not dfs(0, parent):
        return False
    if any(not visited[i] for i in range(num_vertices)):
        return False
    return True

# Follow algorithm BB
E_BB = []
biconnected = False
for edge in edges:
    i, j, _ = edge
    # Add edge and check biconnectivity
    E_BB.append(edge)
    subgraph = [[0] * num_cities for _ in range(num_cities)]
    for e in E_BB:
        subgraph[e[0]][e[1]] = subgraph[e[1]][e[0]] = 1
    if is_biconnected(subgraph, num_cities):
        c_BB = max(e[2] for e in E_BB)
        break

# Step 2: Identifying the tour
# Using a simple heuristic approach via nearest neighbor or alternatively, brute force for small graph
# Brute force: Find all permutations and keep track of the smallest bottleneck tour
best_tour = None
best_max_dist = float('inf')
for perm in permutations(range(1, num_cities)):
    tour = [0] + list(perm) + [0]
    max_dist = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    if max_dist < best_max_dist:
        best_max_dist = max_dist
        best_tour = tour

# Calculate total distance
total_travel_cost = sum(distances[best_tort[i]][best_tour[i+1]] for i in range(len(best_tour)-1))

print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {best_max_dist}")