import math
from itertools import combinations
from collections import defaultdict

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def is_biconnected(vertices, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
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
                if parent[v] == -1 and children > 1:
                    ap_points.add(v)
                elif parent[v] != -1 and low[to] >= tin[v]:
                    ap_points.add(v)

    time = 0
    dfs(vertices[0], 0)
    is_connected = len(visited) == len(vertices)
    is_ap_free = len(ap_points) == 0
    return is_connected and is_ap_free and not bridges

def algorithm_bb(vertices, edges):
    edges_sorted = sorted(edges, key=lambda e: e[2])
    E_BB = set()
    for edge in edges_sorted:
        E_BB.add((edge[0], edge[1]))
        if is_biconnected(vertices, E_BB):
            return E_BB, max(e[2] for e in E_BB)
    return set(), float('inf')

def find_tour(cities, edges):
    tour = [0]
    current = 0
    visited = set([0])
    while len(visited) < len(cities):
        next_edge = min((e for e in edges if e[0] == current and e[1] not in visited), key=lambda e: e[2])
        tour.append(next_edge[1])
        visited.add(next_edge[1])
        current = next_edge[1]
    tour.append(0) # return to the depot
    return tour

cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
          (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
          (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

edges = [(i, j, euclidean_distance(cities[i], cities[j])) for i, j in combinations(range(len(cities)), 2)]

# Use Algorithm BB to find bottleneck-optimal biconnected subgraph
vertices = list(range(len(cities)))
bicon_connected_edges, bottleneck = algorithm_bb(vertices, edges)

# Find Tour
final_tour = find_tour(cities, bicon_connected_edges)

# Calculate distances
total_cost = sum(euclidean_distance(cities[final_tour[i]], cities[final_tour[i+1]]) for i in range(len(final_tour)-1))
max_distance = max(euclidean_distance(cities[final_tour[i]], cities[final_tour[i+1]]) for i in range(len(final_tour)-1))

print("Tour:", final_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)