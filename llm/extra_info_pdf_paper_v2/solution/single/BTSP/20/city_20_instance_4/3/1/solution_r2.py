import math
import heapq
from collections import defaultdict
from sys import maxsize

# City coordinates
city_coords = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate Euclidean distance between two cities
def distance(index1, index2):
    x1, y1 = city_coords[index1]
    x2, y2 = city_coords[index2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Find the Minimum Spanning Tree using Prim's algorithm
def minimum_spanning_tree(num_cities):
    mst_edges = []
    visited = [False] * num_cities
    min_edge = [(0, 0)]  # (cost, start)
    heapq.heapify(min_edge)
    
    mst_cost = 0
    num_edges = 0
    
    while min_edge and num_edges < num_cities:
        cost, u = heapq.heappop(min_edge)
        if visited[u]:
            continue
        
        visited[u] = True
        mst_cost += cost
        num_edges += 1
        
        for v in range(num_cities):
            if not visited[v] and u != v:
                heapq.heappush(min_edge, (distance(u, v), v))
        
        if cost != 0:
            mst_edges.append((u, v))
    
    return mst_edges, mst_cost

# Reconstruct the tour path from MST
def find_tour(mst_edges, start):
    graph = defaultdict(list)
    for u, v in mst_edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Perform DFS to get a tour
    def dfs(current, path):
        path.append(current)
        if len(path) > 1 and path[-1] == path[0]:
            return path
        visited[current] = True
        for neighbor in graph[current]:
            if not visited[neighbor]:
                result = dfs(neighbor, path)
                if result:
                    return result
        path.pop()
        visited[current] = False
        return None
    
    visited = [False] * len(city_coords)
    return dfs(start, [])

# Get data and apply heuristic
mst_edges, mst_cost = minimum_spanning_tree(len(city_coords))
tour = find_tour(mst_edges, 0)

# Calculate metrics
max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)