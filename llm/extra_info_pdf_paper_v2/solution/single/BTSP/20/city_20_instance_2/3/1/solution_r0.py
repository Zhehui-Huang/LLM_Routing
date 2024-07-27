import math
from scipy.spatial import distance_matrix
import numpy as np
from heapq import heappop, heappush

# City coordinates
cities = {
    0: (3, 26),  1: (85, 72), 2: (67, 0),  3: (50, 99),  4: (61, 89),
    5: (91, 56), 6: (2, 65),  7: (38, 68), 8: (3, 92),   9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate distance matrix
points = [cities[i] for i in range(len(cities))]
dist_matrix = distance_matrix(points, points)

# Helper function to compute a MST using Prim's algorithm
def minimum_spanning_tree(num_nodes, graph):
    mst = []
    visited = [False] * num_nodes
    min_edges = [(0, None)]  # (cost, node)
    
    while min_edges:
        cost, u = heappop(min_edges)
        
        if visited[u]:
            continue
        
        visited[u] = True
        mst.append(u)
        
        for v in range(num_nodes):
            if not visited[v] and graph[u][v] != 0:
                heappush(min_edges, (graph[u, v], v))
                
    return mst

# Construct a tour from the MST
def construct_tour(mst, start_node):
    tour = []
    stack = [start_node]
    visited = [False] * len(mst)
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            tour.append(node)
            for i in range(len(mst) - 1, -1, -1):
                if not visited[mst[i]]:
                    stack.append(mst[i])
    tour.append(start_node)  # complete the tour by coming back to start
    return tour

# Minimum spanning tree (for cities including the depot)
mst = minimum_spanning_tree(len(cities), dist_matrix)
tour = construct_tour(mst, 0)

# Calculate total cost and maximum distance between consecutive cities
total_cost, max_dist = 0, 0
last_city = tour[0]
for city in tour[1:]:
    travel_cost = dist_matrix[last_city, city]
    total_cost += travel_cost
    if travel_cost > max_dist:
        max_dist = travel_dost
    last_city = city

output_tour = tour
output_total_cost = total_cost
output_max_distance = max_dist

print(f"Tour: {output_tour}")
print(f"Total travel cost: {output_total_cost}")
print(f"Maximum distance between consecutive cities: {output_max_distance}")