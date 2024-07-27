import math
from scipy.spatial import distance_matrix
import numpy as np

# Coordinates for depot and cities
cities = [
    (3, 26),  # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14),
    (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Create distance matrix
dist_matrix = distance_matrix(cities, cities)

# Function to find the minimum spanning tree using Prim's Algorithm
def prim_mst(n, dist_matrix):
    connected = set()
    edges = []
    connected.add(0)
    mst_edges = []
    while len(connected) < n:
        crossing = [(dist_matrix[u][v], u, v) for u in connected for v in range(n) if v not in connected]
        weight, frm, to = min(crossing)
        connected.add(to)
        mst_edges.append((frm, to, weight))
        edges.append(weight)
    return mst_edges, edges

# Function to calculate a tour from the MST
def mst_to_tour(n, mst_edges):
    from collections import defaultdict, deque

    # Build adjacency list from MST edges
    graph = defaultdict(list)
    for u, v, _ in m2_edges:
        graph[u].append(v)
        graph[v].append(u)

    # Perform a DFS to get the tour path
    tour = []
    stack = [0]
    seen = set()
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        tour.append(node)
        seen.add(node)
        for adj in graph[node]:
            if adj not in seen:
                stack.append(adj)

    # Close the tour by returning to the start
    tour.append(0)
    return tour

n = len(cities)  # number of cities

# Compute the MST
m2_edges, edges = prim_mst(n, dist_matrix)

# Get a tour from the MST
tour = mst_to_tour(n, m2_edges)

# Calculate tour cost and max edge cost
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    city_from = tour[i-1]
    city_to = tour[i]
    dist = dist_matrix[city_from][city_to]
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")