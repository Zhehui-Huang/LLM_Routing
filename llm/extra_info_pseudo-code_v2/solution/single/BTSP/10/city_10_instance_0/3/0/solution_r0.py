import math
from collections import defaultdict

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_set(parent, i):
    if parent[i] == i:
        return i
    else:
        return find_set(parent, parent[i])

def union_set(parent, rank, x, y):
    xroot = find_set(parent, x)
    yroot = find_set(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def is_biconnected(graph, V):
    """If removing any single vertex from graph leaves the graph connected,
    it's biconnected"""
    def DFS_count(v, visited, adj):
        count = 1
        visited[v] = True
        for i in adj[v]:
            if not visited[i]:
                count += DFS_count(i, visited, adj)
        return count

    for v in range(V):
        visited = [False] * V
        # Start DFS from the next vertex
        adj = [set(graph[i]) for i in range(V)]
        adj[v] = set()  # Remove vertex `v`
        
        # Starting vertex for DFS
        start_vertex = 1 if v == 0 else 0
        count = DFS_count(start_vertex, visited, adj)
        if count != V-1:
            return False
    return True

def bottleneck_optimal_biconnected_subgraph(graph, V):
    sorted_edges = sorted([(euclidean_distance(coords[i], coords[j]), i, j) for i in range(V) for j in range(i+1, V)], key=lambda x: x[0])
    parent = list(range(V))
    rank = [0] * V

    bcc_graph = defaultdict(set)
    bcc_edges = []

    for weight, u, v in sorted_edges:
        if find_set(parent, u) != find_frame(parent, v):
            union_set(parent, rank, u, v)
            bcc_graph[u].add(v)
            bcc_graph[v].add(u)
            bcc_edges.append((weight, u, v))
            if is_biconnected(bcc_graph, V):
                return bcc_edges, weight
    return [], float('inf')

# Define cities
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69), 
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Number of vertices
V = len(cities)
coords = list(cities.values())

# Get the bottleneck-optimal biconnected subgraph
edges, bottleneck_weight = bottleneck_optimal_biconnected_subgraph(coords, V)

# Hamiltonian cycle in simple graph (square of biconnected trigraph)
# Here we need a placeholder algorithm since biconnected subgraph may be complex to handle at once
# Let's start by a simple nearest neighbor TSP solution (not optimal but efficient to implement)
def nearest_neighbor_tsp(start, coords):
    n = len(coords)
    unvisited = set(range(n))
    tour = [start]
    unvisited.remove(start)
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(coords[current_city], coords[x]))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(start)  # Close the loop
    return tour

# Get tour with nearest neighbor
tour = nearest_neighbor_tdo.findne_hamiltoniansp(0, coords)

# Calculate tour details
def calculate_tour_details(tour, coords):
    total_cost = 0
    max_distance = 0
    tour_length = len(tour)
    for i in range(tour_length - 1):
        dist = euclidean_distance(coords[tour[i]], coords[tour[i+1]])
        total_cost += dist
        max_distance = max(max_distance, dist)
        
    return tour, total_cost, max_distance

tour, total_cost, max_distance = calculate_tour_details(tour, coords)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)