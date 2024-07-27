import math
import itertools

# City coordinates as tuples (x, y)
cities = [
    (8, 11),  # City 0 (Depot)
    (40, 6),  # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),  # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)  # City 19
]

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate all pairs of distances between cities
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Heuristic Solution: Minimum Spanning Tree + DFS to form a tour and then double the edges
def mst_prim(cities, distances):
    import heapq

    n = len(cities)
    visited = [False] * n  # Track visited cities
    min_edge = [(float('inf'), -1) for _ in range(n)]  # Store minimum weight edge to each vertex
    min_edge[0] = (0, 0)  # Start from the depot, city 0
    mst = []
    pq = [(0, 0)]  # priority queue storing (cost, vertex)
    
    total_cost = 0
    
    while pq:
        cost, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        
        visited[u] = True
        total_cost += cost
        if min_edge[u][1] != u:
            mst.append((min_edge[u][1], u))
        
        for v in range(n):
            if not visited[v] and distances[u][v] < min_edge[v][0]:
                min_edge[v] = (distances[u][v], u)
                heapq.heappush(pq, (distances[u][v], v))
                
    return mst, total_cost

# Find Minimum Spaning Tree
mst, _ = mst_prim(cities, distances)

# Convert MST to adjacency list
adj_list = [[] for _ in range(len(cities))]
for u, v in mst:
    adj_list[u].append(v)
    adj_list[v].append(u)

# Perform a DFS to obtain a tour starting and ending at the depot (city 0)
def dfs_tour(city, visited, path, adj_list):
    visited[city] = True
    path.append(city)
    for neighbor in adj_list[city]:
        if not visited[neighbor]:
            dfs_tour(neighbor, visited, path, adj_list)

# Create the tour using DFS
visited_cities = [False] * len(cities)
path = []
dfs_tour(0, visited_cities, path, adj_list)
path.append(0) # return to the depot

# Evaluate the tour
def evaluate_tour(tour, distances):
    max_distance = 0
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        dist = distances[tour[i]][tour[i + 1]]
        total_travel_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_travel_cost, max_distance

total_cost, max_dist = evaluate_tour(path, distances)

print("Tour:", path)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)