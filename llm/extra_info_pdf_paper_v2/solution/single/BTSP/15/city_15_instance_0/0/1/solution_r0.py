import numpy as np
from scipy.spatial.distance import euclidean
from heapq import heappush, heappop
from collections import defaultdict

# City coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50),
    (21, 23), (88, 59), (79, 77), (63, 23),
    (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

# Calculate distances
def calculate_distances(cities):
    n = len(cities)
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            distances[i][j] = distances[j][i] = euclidean(cities[i], cities[j])
    return distances

distances = calculate_positions(cities)

# Prim's algorithm to find the Minimum Spanning Tree with focus on edge bottle-necks
def minimum_spanning_tree(distances):
    num_cities = len(distances)
    in_tree = [False] * num_cities
    min_edge = [(float('inf'), -1)] * num_cities
    mst = []
    min_edge[0] = (0, 0)  # Start with city 0
    
    heap = []
    heappush(heap, (0, 0))  # (cost, city)
    
    while heap:
        cost, u = heappop(heap)
        if in_tree[u]:
            continue
        in_tree[u] = True
        mst.append((min_edge[u][1], u, cost))
        
        for v in range(num_cities):
            if not in_tree[v] and distances[u][v] < min_edge[v][0]:
                min_edge[v] = (distances[u][v], u)
                heappush(heap, (distances[u][v], v))
    
    return mst

mst = minimum_spanning_tree(distances)

# Constructing the tour from the MST
def construct_tour_from_mst(mst, start_node):
    graph = defaultdict(list)
    for u, v, _ in mst:
        if u != -1:
            graph[u].append(v)
            graph[v].append(u)
    
    tour = []
    visit_order = []
    
    def dfs(node, parent):
        tour.append(node)
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs(neighbor, node)
        tour.append(node)
    
    dfs(0, -1)
    tour = list(dict.fromkeys(tour))  # Remove duplicates while preserving order
    if tour[-1] != start_node:
        tour.append(start_node)  # Ensure the tour ends at the start node
    
    return tour

tour = construct_tour_from_mst(mst, 0)

# Calculate total cost and maximum distance between consecutive cities
def evaluate_tour(tour, distances):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        cost = distances[tour[i]][tour[i+1]]
        total_cost += cost
        max_distance = max(max_distance, cost)
    return total_cost, max_distance

total_cost, max_distance = evaluate_tour(tour, distances)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)