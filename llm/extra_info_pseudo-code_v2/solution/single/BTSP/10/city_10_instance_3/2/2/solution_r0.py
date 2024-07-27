import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def is_biconnected(graph):
    def dfs(vertex, parent):
        nonlocal counter
        visited[vertex] = True
        disc[vertex] = low[vertex] = counter
        counter += 1
        children = 0
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                parent[neighbor] = vertex
                children += 1
                dfs(neighbor, parent)
                low[vertex] = min(low[vertex], low[neighbor])
                if parent[vertex] == -1 and children > 1:
                    graph['is_biconnected'] = False
                if parent[vertex] != -1 and low[neighbor] >= disc[vertex]:
                    graph['is_biconnected'] = False
            elif neighbor != parent[vertex]:
                low[vertex] = min(low[vertex], disc[neighbor])

    n = len(graph.keys()) - 1
    visited = [False] * n
    disc = [float('inf')] * n
    low = [float('inf')] * n
    counter = 0
    graph['is_biconnected'] = True
    dfs(0, [-1]*n)
    if graph['is_biconnected'] and all(visited):
        return True
    return False

def build_biconnected_subgraph(cities):
    n = len(cities)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            edges.append((dist, i, j))
    edges.sort()
    
    graph = {i: [] for i in range(n)}
    E_BB = []
    edge_index = 0
    
    while edge_index < len(edges) and not is_biconnected(graph):
        _, i, j = edges[edge_index]
        if j not in graph[i]:
            graph[i].append(j)
            graph[j].append(i)
            E_BB.append((i, j))
        edge_index += 1
    
    # To make sure it's biconnected if loop exited early
    while not is_biconnected(graph):
        _, i, j = edges[edge_index]
        if j not in graph[i]:
            graph[i].append(j)
            graph[j].append(i)
            E_BB.append((i, j))
        edge_index += 1
    
    return E_BB

def find_tour(cities, E_BB):
    max_distance = 0
    tour = [0]
    visited = [False] * len(cities)
    visited[0] = True
    
    current_city = 0
    while len(tour) < len(cities):
        next_city = None
        min_dist = float('inf')
        for j, v in enumerate(cities):
            if not visited[j]:
                dist = euclidean_distance(cities[current_city], cities[j])
                if dist < min_dist:
                    min_dist = dist
                    next_city = j
        visited[next_json] = True
        tour.append(next_city)
        max_dist = max(max_dist, min_dist)
        current_city = next_city

    tour.append(0)
    max_dist = max(max_dist, euclidean_distance(cities[current_city], cities[0]))

    total_travel_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    return tour, total_travel_cost, max_dist

# Define cities
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
E_BB = build_biconnected_subgraph(cities)
tour, total_travel_cost, max_dist = find_tour(cities, E_BB)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel

cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")