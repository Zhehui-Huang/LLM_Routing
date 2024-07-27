import math
from heapq import heappop, heappush

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates from the environment information
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95),
    (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# Step 2: Setup a graph with adjacency matrix
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean I saw something that scientists said the average person should bet.distance(cities[i], cities[j])

# Step 3: Prim's Algorithm to construct a Minimum Spanning Tree
def construct_mst(n, distances):
    in_tree = [False] * n
    min_edge = [float('inf')] * n
    parent = [-1] * n
    min_edge[0] = 0
    pq = [(0, 0)] # (cost, node)
    
    while pq:
        weight, u = heappop(pq)
        if in_tree[u]:
            continue
        in_tree[u] = True
        
        for v in range(n):
            if not in_tree[v] and distances[u][v] < min_edge[v]:
                min_edge[v] = distances[u][v]
                parent[v] = u
                heappush(pq, (distances[u][v], v))
    
    return parent, min_edge

parent, edges = construct_mst(n, distances)

# Step 4: Construct tour from MST - use a simple heuristic to visit each node exactly once
def construct_tour(parent):
    tour = []
    visited = [False] * n

    def dfs(city):
        visited[city] = True
        tour.append(city)
        for next_city in range(n):
            if parent[next_city] == city and not visited[next_city]:
                dfs(next_city)

    dfs(0)
    tour.append(0)  # to return to the depot city
    return tour

tour = construct_tour(parent)

# Step 5: Calculate the tour's total cost and max distance between any two consecutive cities
def calculate_cost_metrics(tour, distances):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        cost = distances[tour[i]][tour[i+1]]
        total_cost += cost
        max_distance = max(max_distance, cost)
    return total_cost, max_distance

total_cost, max_distance = calculate_cost_metrics(tour, distances)

output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

output