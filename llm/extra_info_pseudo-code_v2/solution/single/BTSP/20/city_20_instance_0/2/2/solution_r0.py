import math
from itertools import combinations, permutations

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Euclidean distance function
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Building the graph with distance matrix
dist_matrix = {}
for i, j in combinations(cities, 2):
    dist = euclidean_distance(cities[i], cities[j])
    dist_matrix[(i, j)] = dist
    dist_matrix[(j, i)] = dist

# Sorting the edges by weight
edges = sorted(dist_matrix.items(), key=lambda x: x[1])

# Create a function to check if the graph is biconnected
def is_biconnected(graph, V):
    # A simple DFS based function to check connectivity
    def dfs(u, parent, discovery, low, ap, bridges):
        nonlocal time
        children = 0
        visited[u] = True
        discovery[u] = low[u] = time
        time += 1
    
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                dfs(v, parent, discovery, low, ap, bridges)
                low[u] = min(low[u], low[v])
                
                # Check if the edge u-v is a bridge
                if low[v] > discovery[u]:
                    bridges.append((u, v))
                
            elif v != parent[u]:
                low[u] = min(low[u], discovery[v])
    
    V = len(V)
    visited = [False] * V
    discovery = [0] * V
    low = [0] * V
    parent = [-1] * V
    bridges = []
    time = 0
    
    # Calling DFS for all unvisited vertices
    for i in range(V):
        if not visited[i]:
            dfs(i, parent, discovery, low, [], bridges)
    
    return len(bridges) == 0

# Applying the BB algorithm
def bb_algorithm(edges):
    graph = {i: set() for i in cities}
    current_edges = []
    for ((u, v), dist) in edges:
        graph[u].add(v)
        graph[v].add(u)
        current_edges.append(((u, v), dist))
        if is_biconnected(graph, cities.keys()):
            break
    
    return current_edges

# Finding the Bottleneck-optimal Biconnected Subgraph
biconnected_subgraph_edges = bb_experiment(edges)
biconnected_subgraph = {i: set() for i in cities}
for ((u, v), _) in biconnected_subgraph_edges:
    biconnected_subgraph[u].add(v)
    biconnected_subgraph[v].add(u)

# Finding the Hamiltonian cycle
# Heuristic: Use a simple nearest neighbor strategy modified for the availability of edges in the biconnected subgraph
def find_tour(start, graph):
    visited = {i: False for i in graph}
    tour = [start]
    max_distance = 0
    total_cost = 0
    current = start
    visited[start] = True
    
    while len(tour) < len(cities):
        next_city = min((c for c in graph[current] if not visited[c]), key=lambda x: dist_matrix[(current, x)])
        visited[next_city] = True
        tour.append(next_city)
        dist = dist_matrix[(current, next_city)]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
        current = next_city
    
    # Return to start
    tour.append(start)
    total_cost += dist_matrix[(current, start)]
    max_distance = max(max_distance, dist_matrix[(current, start)])
    
    return tour, total_cost, max_distance

tour, total_cost, max_distance = find_tour(0, biconnected_subgraph)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)