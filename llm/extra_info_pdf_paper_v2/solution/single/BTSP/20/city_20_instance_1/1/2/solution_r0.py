import numpy as np
from scipy.spatial.distance import euclidean
from heapq import heappush, heappop

# Define cities coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

num_cities = len(cities)

# Compute the distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean(cities[i], cities[j])
        distance_matrix[i, j] = distance_matrix[j, i] = dist

# Helper function to find minimum bottleneck spanning tree (MST) using a modified Prim's Algorithm
def minimum_bottleneck_spanning_tree(distance_matrix):
    num_vertices = len(distance_matrix)
    in_tree = [False] * num_vertices
    min_edge = [float('inf')] * num_vertices
    parent = [-1] * num_vertices
    edges = []
    
    # Start with vertex 0
    min_edge[0] = 0
    
    for _ in range(num_vertices):
        u = -1
        for v in range(num_vertices):
            if not in_tree[v] and (u == -1 or min_edge[u] > min_edge[v]):
                u = v
        in_tree[u] = True
        
        if parent[u] != -1:
            edges.append((parent[u], u, min_edge[u]))
        
        for v in range(num_vertices):
            if distance_matrix[u][v] < min_edge[v] and not in_tree[v]:
                min_edge[v] = distance_matrix[u][v]
                parent[v] = u
                
    return edges, parent

# Build minimum bottleneck spanning tree
edges, parent = minimum_bottleneck_spanning_tree(distance_matrix)

# Transform MST to a full cycle by DFS traversal
def dfs_cycle(start, parent):
    stack = [start]
    visited = [False] * len(parent)
    cycle = []
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        cycle.append(node)
        for i in range(len(parent)):
            if parent[i] == node and not visited[i]:
                stack.append(i)
    return cycle

# Get the cycle path from parent array
tour = dfs_cycle(0, parent)
tour.append(0)  # Complete the cycle by returning to the start point

# Calculate total travel cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    this_cost = distance_matrix[tour[i-1]][tour[i]]
    total_cost += this_cost
    if this_cost > max_distance:
        max_distance = this_cost

output = f"Tour: {tour}\nTotal travel cost: {total_cost:.2f}\nMaximum distance between consecutive cities: {max_distance:.2f}"
print(output)