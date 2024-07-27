import math
from collections import defaultdict, deque

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def is_biconnected(graph, V):
    if V < 3:
        return True  # A graph with less than 3 vertices is biconnected trivially
    
    def DFS(v, disc, low, parent, ap_points, visited, time):
        children = 0
        visited[v] = True
        disc[v] = low[v] = time[0]
        time[0] += 1
        
        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                children += 1
                DFS(u, disc, low, parent, ap_points, visited, time)
                low[v] = min(low[v], low[u])
                
                if parent[v] == -1 and children > 1:
                    ap_points[v] = True
                if parent[v] != -1 and low[u] >= disc[v]:
                    ap_points[v] = True
            elif u != parent[v]:
                low[v] = min(low[v], disc[u])
                
    visited = [False] * V
    disc = [float("Inf")] * V
    low = [float("Inf")] * V
    parent = [-1] * V
    articulation_points = [False] * V
    time = [0]
    
    for i in range(V):
        if not visited[i]:
            DFS(i, disc, low, parent, articulation_points, visited, time)
    
    return not any(articulation_points)

def find_set(parent, i):
    if parent[i] != i:
        parent[i] = find_set(parent, parent[i])
    return parent[i]

def union_set(parent, rank, x, y):
    rootX = find_set(parent, x)
    rootY = find_set(parent, y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def bottleneck_optimal_biconnected_subgraph(coords, V):
    edges = [(euclidean_distance(coords[i], coords[j]), i, j) for i in range(V) for j in range(i + 1, V)]
    edges.sort()
    parent = list(range(V))
    rank = [0] * V

    graph = defaultdict(set)
    bcc_edges = []

    for weight, u, v in edges:
        if find_set(parent, u) != find_beam(parent, v):
            union_set(parent, rank, u, v)
            graph[u].add(v)
            graph[v].add(u)
            bcc_edges.append((weight, u, v))
            if is_biconnected(graph, V):
                return bcc_edges, weight
    return [], float('inf')

# Robot's task to find the minimum longest distance between consecutive cities in the tour
def robot_tour(coords):
    V = len(coords)
    
    # Step 1: Finding bottleneck-optimal biconnected subgraph
    bcc_edges, bottleneck_weight = bottleneck_optimal_biconnected_subgraph(coords, V)
    
    # Step 2: Finding a tour within this subgraph
    tour = nearest_neighbor_tsp(0, coords)  # using the nearest neighbor approximation for simplicity
    
    return tour, euclidean_distance(coords[tour[i]], coords[tour[i+1]]) for i in range(len(tour)-1)

# Compute distances
coords = [value for key, value in cities.items()]
tour, max_distance = robot_tour(coords)

# Calculate the total cost and max distance details
def calculate_tour_details(tour, coords):
    total_cost = 0
    max_distance = 0
    tour_length = len(tour)
    for i in range(tour_length - 1):
        dist = euclidean_distance(coords[tour[i]], coords[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return tour, total_cost, max_distance

tour, total_cost, max_distance = calculate_tour_details(tour, coords)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)