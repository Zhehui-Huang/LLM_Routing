import math
import itertools
from scipy.spatial import distance_matrix
from heapq import heappop, heappush

def calculate_distance(c1, c2):
    return math.hypot(c1[0] - c2[0], c1[1] - c2[1])

# Defining the cities' coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82), 
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23), 
    (78, 76), (68, 45), (50, 28), (69, 9)
]

def prim_mst(cities):
    n = len(cities)
    visited = [False] * n
    # Min-heap to pick the edge with the smallest distance
    min_heap = [(0, 0, 0)]  # Cost, Start, End
    mst_edges = []
    
    while min_heap:
        cost, frm, to = heappop(min_heap)
        if visited[to]:
            continue
        visited[to] = True
        mst_edges.append((frm, to, cost))
        for next_city in range(n):
            if not visited[next_city]:
                distance = calculate_distance(cities[to], cities[next_city])
                heappush(min_heap, (distance, to, next_city))
    return mst_edges

# To create a cycle from MST
def find_tour(mst, n):
    graph = {i: [] for i in range(n)}
    for frm, to, cost in mst:
        graph[frm].append((to, cost))
        graph[to].append((frm, cost))
    
    # Use a DFS to get the tour path
    path = []
    visited = [False] * n

    def dfs(v):
        visited[v] = True
        path.append(v)
        for (next_v, cost) in graph[v]:
            if not visited[next_v]:
                dfs(next_v)
    
    dfs(0)  # Considering city 0 as the starting point
    path.append(0)  # making it a cycle ending at the starting point
    return path

def tour_cost_and_bottleneck(tour, cities):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_distance(cities[tour[i - 1]], cities[tour[i]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

# Create the MST
mst_edges = prim_mst(cities)
tour = find_tour(mst_edges, len(cities))

# Calculate cost and bottleneck
total_travel_cost, max_distance = tour_cost_and_bottleneck(tour, cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")