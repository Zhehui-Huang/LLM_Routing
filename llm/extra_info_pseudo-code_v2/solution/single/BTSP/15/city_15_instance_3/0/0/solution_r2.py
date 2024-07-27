import math
from itertools import combinations
from collections import defaultdict

# Function to calculate the Euclidean distance between two cities given their coordinates
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Function to verify if a graph is biconnected
def is_biconnected(vertices, edges):
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    visited = set()
    tin = [-1] * len(vertices)
    low = [-1] * len(vertices)
    parent = [-1] * len(vertices)
    ap_points = set()
    bridges = []
    
    def dfs(v, discovery_time):
        nonlocal time
        visited.add(v)
        tin[v] = low[v] = time
        time += 1
        children = 0
        
        for to in graph[v]:
            if to == parent[v]:
                continue
            if to in visited:
                low[v] = min(low[v], tin[to])
            else:
                parent[to] = v
                children += 1
                dfs(to, discovery_time)
                low[v] = min(low[v], low[to])
                
                # Bridge condition
                if low[to] > tin[v]:
                    bridges.append((v, to))
                
                # Articulation point condition
                if parent[v] == -1 and children > 1 or (parent[v] != -1 and low[to] >= tin[v]):
                    ap_points.add(v)
    
    for v in vertices:
        if v not in visited:
            time = 0
            dfs(v, 0)
    
    is_connected = len(visited) == len(vertices)
    is_ap_free = len(ap_points) == 0
    return is_connected and is_ap_free and not bridges

# Helper function to implement Algorithm BB
def algorithm_bb(vertices, edges):
    edges_sorted = sorted(edges, key=lambda e: e[2])
    E_BB = set()
    for u, v, w in edges_sorted:
        E_BB.add((u, v))
        if is_biconnected(vertices, E_BB):
            return E_BB, max(current_edge[2] for current_edge in edges if (current_edge[0], current_edge[1]) in E_BB)
    return set(), float('inf')

# Helper function to generate a tour using edges specified
def find_tour(cities, edges):
    tour = [0]
    current = 0
    visited = {0}
    while len(visited) < len(cities):
        # Find the next edge with minimum weight that leads to an unvisited city
        next_edge = min((e for e in edges if e[0] == current and e[1] not in visited), key=lambda e: e[2])
        current = next_edge[1]
        tour.append(current)
        visited.add(current)
    tour.append(0)  # returning to the starting city
    return tour

# Defining the cities with their coordinates
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
          (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
          (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Computing all possible edges and their weights
edges = [(i, j, euclidean_distance(cities[i], cities[j])) for i, j in combinations(range(len(cities)), 2)]

# Applying Algorithm BB to compute bottleneck-optimal biconnected subgraph
vertices = list(range(len(cities)))
biconnected_edges, bottleneck = algorithm_bb(vertices, edges)

# Formulating the edges list for the tour construction
used_edges = [(u, v, w) for u, v, w in edges if (u, v) in biconnected_edges or (v, u) in biconnected_edges]

# Generating the tour based on the biconnected subgraph
final_tour = find_tour(cities, used_edges)

# Calculating the total cost and the maximum distance between consecutive cities
total_cost = sum(euclidean_distance(cities[final_tour[i]], cities[final_tour[i+1]]) for i in range(len(final_tour) - 1))
max_distance = max(euclidean_distance(cities[final_tour[i]], cities[final_tour[i+1]]) for i in range(len(final_tour) - 1))

print("Tour:", final_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)