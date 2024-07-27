import math
import itertools
from collections import defaultdict

# City coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generating all possible edges with their weights
def calculate_edges():
    num_vertices = len(coordinates)
    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            edges.append((i, j, dist))
            edges.append((j, i, dist))
    return edges, num_vertices

def dfs(u, visited, disc, low, parent, ap, graph, time):
    children = 0
    visited[u] = True
    disc[u] = low[u] = time[0]
    time[0] += 1
    
    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            children += 1
            dfs(v, visited, disc, low, parent, ap, graph, time)
            low[u] = min(low[u], low[v])
            if parent[u] is None and children > 1:
                ap[u] = True
            if parent[u] is not None and low[v] >= disc[u]:
                ap[u] = True
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])

def is_biconnected(graph, V):
    visited = [False] * V
    disc = [float("Inf")] * V
    low = [float("Inf")] * V
    parent = [None] * V
    ap = [False] * V
    time = [0]
    
    for i in range(V):
        if not visited[i]:
            dfs(i, visited, disc, low, parent, ap, graph, time)
            if visited.count(True) != V:
                return False
            if True in ap:
                return False
    return True

def find_biconnected_subgraph(edges, V):
    sorted_edges = sorted(edges, key=lambda x: x[2])
    graph = defaultdict(list)

    for u, v, _ in sorted_edges:
        graph[u].append(v)
        graph[v].append(u)
        if is_biconnected(graph, V):
            last_u, last_v, max_edge_weight = u, v, _
            return graph, max_edge_weight
    return None, None

# Given a biconnected graph, find a Hamiltonian cycle as an approximation
def find_hamiltonian_cycle(graph, V):
    start = 0
    visited = set([start])
    tour = [start]
    
    while len(visited) < V:
        last = tour[-1]
        for neighbor in graph[last]:
            if neighbor not in visited:
                visited.add(neighbor)
                tour.append(neighbor)
                break
    
    tour.append(start) # to complete the cycle
    return tour

def calculate_tour_cost(tour):
    total_cost = 0
    max_dist = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        total_cost += dist
        max_dist = max(max_dist, dist)
    return total_cost, max_dist

edges, num_vertices = calculate_edges()
bic_graph, max_edge_weight = find_biconnected_subgraph(edges, num_vertices)
if bic_graph:
    tour = find_hamiltonian_cycle(bic_graph, num_vertices)
    total_cost, max_dist = calculate_tour_cost(tour)
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_dist)
else:
    print("No biconnected subgraph found, cannot construct a valid tour")