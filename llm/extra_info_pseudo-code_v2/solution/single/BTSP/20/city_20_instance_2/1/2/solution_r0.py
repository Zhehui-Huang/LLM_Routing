import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def compute_distances(cities):
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean_dist(cities[i], cities[j])
    return distances

def is_biconnected(graph, n):
    start_vertex = 0
    visited = [False] * n
    disc = [float("Inf")] * n
    low = [float("Inf")] * n
    parent = [-1] * n
    
    def bridge_util(u):
        nonlocal time
        visited[u] = True
        disc[u] = low[u] = time
        time += 1
        for v in range(n):
            if graph[u][v]: # If u-v is connected in the graph
                if not visited[v]:
                    parent[v] = u
                    bridge_util(v)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        return False
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
        return True
    
    time = 0
    if not bridge_util(start_vertex):
        return False
    if any(not visited[i] for i in range(n)):
        return False
    return True

def find_bottleneck_optimal_biconnected_subgraph(cities):
    n = len(cities)
    all_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            all_edges.append((i, j, euclidean_dist(cities[i], cities[j])))

    all_edges.sort(key=lambda x: x[2])
    g = [[0]*n for _ in range(n)]
    selected_edges = []
    
    for edge in all_edges:
        u, v, _ = edge
        g[u][v] = g[v][u] = 1
        if not is_biconnected(g, n):
            g[u][v] = g[v][u] = 0
        else:
            selected_edges.append(edge)

    return g, max(e[2] for e in selected_edges)

def calculate_optimal_tour_approximation(g, n):
    # A simple approximation approach could be the nearest neighbour since we need an example
    visited = [False] * n
    tour = [0]
    current = 0
    visited[0] = True
    total_cost = 0
    max_distance = 0
    while len(tour) < n:
        next_city = None
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and g[current][i] != 0 and g[current][i] < min_dist:
                next_city = i
                min_dist = g[current][i]
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_dist
        if min_dist > max_distance:
            max_distance = min_dist
        current = next_city
    # Close the cycle
    final_leg = euclidean_dist(cities[tour[-1]], cities[tour[0]])
    total_cost += final_leg
    if finalleg > max_distance:
        max_distance = final_leg
    tour.append(0)
    return tour, total_cost, max_distance

# Initialized city coordinates
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92),
          (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
          (51, 58), (30, 48)]

# Finding Bottleneck Optimal Biconnected Subgraph
biconnected_subgraph, bottleneck_cost = find_bottleneck_optimal_biconnected_subgraph(cities)

# Finding the optimal tour with approximation
tour, total_travel_cost, max_distance = calculate_optimal_tour_approximation(biconnected_subgraph, len(cities))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")