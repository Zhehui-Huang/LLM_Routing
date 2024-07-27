import math
from scipy.spatial import distance_matrix
import numpy as np

# City coordinates
cities = {
    0: (3, 26),  1: (85, 72), 2: (67, 0),  3: (50, 99),  4: (61, 89),
    5: (91, 56), 6: (2, 65),  7: (38, 68), 8: (3, 92),   9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate distance matrix
points = [cities[i] for i in range(20)]
dist_matrix = distance_matrix(points, points)

# Helper function to calculate Euclidean distance
def euc_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Prim's algorithm for MST
def mst_prim(num_nodes, graph):
    mst_set = [False] * num_nodes
    parent = [None] * num_nodes
    key = [float('inf')] * num_nodes
    key[0] = 0
    mst = []
    
    for _ in range(num_nodes):
        u = min((k, i) for i, k in enumerate(key) if not mst_set[i])[1]
        mst_set[u] = True
        mst.append(u)
        
        for v in range(num_nodes):
            if graph[u][v] > 0 and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
    
    return parent

# Construct tour from MST
def construct_tour_from_mst(num_nodes, parent, start_node):
    tour = []
    visited = [False] * num_nodes
    stack = [start_node]
    
    while stack:
        u = stack.pop()
        tour.append(u)
        for v in range(num"]);

        for v, p in enumerate(parent):
            if p == u and not visited[v]:
                stack.append(v)
                visited[v] = True
        visited[u] = True
    tour.append(start_node)
    return tour

# Computing MST
mst_parents = mst_prim(len(cities), dist_matrix)
tour = construct_tour_from_mst(len(cities), mst_parents, 0)

# Calculate total cost and maximum distance
total_travel_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_consecutive_distance = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_consecutive_result}")