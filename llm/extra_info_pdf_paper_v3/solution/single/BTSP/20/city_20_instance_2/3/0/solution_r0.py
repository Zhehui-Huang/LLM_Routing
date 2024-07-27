import math
from heapq import heappop, heappush

# Defining the cities with their coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Using Prim's algorithm to find the Minimum Spanning Tree
def prim_mst(cities):
    n = len(cities)
    adj = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(cities[i], cities[j])
            adj[i].append((dist, j))
            adj[j].append((dist, i))

    in_mst = [False] * n
    min_edge = [(float('inf'), -1)] * n
    mst_edges = []
    min_edge[0] = (0, 0)
    min_heap = [(0, 0)]
    
    while min_heap:
        d, u = heappop(min_heap)
        if in_mst[u]:
            continue
        
        in_mst[u] = True
        if min_edge[u][1] != u:
            mst_edges.append((u, min_edge[u][1], d))
        
        for weight, v in adj[u]:
            if not in_mst[v] and weight < min_edge[v][0]:
                min_edge[v] = (weight, u)
                heappush(min_heap, (weight, v))
    
    return mst_edges

mst = prim_mst(cities)

# Create a tour by a simple DFS traversal of the MST
def mst_to_tour(start, mst_edges, n):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for u, v, _ in mst_edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(v):
        visited.add(v)
        result.append(v)
        for ne in graph[v]:
            if ne not in visited:
                dfs(ne)
                result.append(v)  # return to the starting node to simulate a complete tour
    
    visited = set()
    result = []
    dfs(start)
    return result

tour = mst_to_tour(0, mst, len(cities))

# Calculate total travel cost and the maximum distance between consecutive cities
def calculate_tour_cost(tour, cities):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = distance(cities[tour[i-1]], cities[tour[i]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

total_cost, max_distance = calculate_tour_cost(tour, cities)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")