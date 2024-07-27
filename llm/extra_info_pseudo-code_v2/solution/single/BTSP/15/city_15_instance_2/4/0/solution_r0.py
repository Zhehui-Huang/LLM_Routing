import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_matrix(coords):
    n = len(coords)
    dist_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclideanDistance(coords[i], coords[j])
    return dist_matrix

def is_biconnected(graph, n):
    # A simple test for biconnectivity: check connectivity and count articulation points
    # This method can be improved with specific algorithms for biconnectivity
    visited = [False] * n
    discovery = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    ap = [False] * n  # Articulation points
    count = 0
    
    def dfs(u):
        nonlocal count
        children = 0
        visited[u] = True
        discovery[u] = low[u] = count
        count += 1
        
        for v in range(n):
            if graph[u][v] != 0:  # There's an edge u-v
                if not visited[v]:
                    parent[v] = u
                    children += 1
                    dfs(v)
                    
                    low[u] = min(low[u], low[v])
                    
                    if parent[u] == -1 and children > 1:
                        ap[u] = True
                    if parent[u] != -1 and low[v] >= discovery[u]:
                        ap[u] = True
                elif v != parent[u]:
                    low[u] = min(low[u], discovery[v])
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            if any(visited) and any(not v for v in visited):
                return False  # Not connected
    return not any(ap)

def construct_biconnected_subgraph(dist_matrix):
    n = len(dist_matrix)
    edges = [(i, j, dist_matrix[i][j]) for i in range(n) for j in range(i+1, n)]
    edges.sort(key=lambda x: x[2])

    graph = [[0] * n for _ in range(n)]
    for u, v, d in edges:
        graph[u][v] = graph[v][u] = d
        if is_biconnected(graph, n):
            return graph, d
        graph[u][v] = graph[v][u] = 0  # Remove if not biconnected
    return None, None  # Should never reach here in usual cases

def find_tour_in_biconnected_subgraph(graph, n):
    tour = []

    def dfs(current, visited):
        visited[current] = True
        tour.append(current)
        for neighbor in range(n):
            if graph[current][neighbor] != 0 and not visited[neighbor]:
                dfs(neighbor, visited)
                break

    visited = [False] * n
    dfs(0, visited)
    tour.append(0)  # Complete the tour by returning to the depot
    return tour

def calculate_tour_costs(tour, dist_matrix):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = dist_matrix[tour[i]][tour[i+1]]
        total_cost += d
        max_distance = max(max_distance, d)
    return total_cost, max_distance

# Coordinates for the cities including the depot
coords = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
          (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

# Step 0: Create the graph
dist_matrix = create_distance_matrix(coords)

# Step 1: Construct a bottleneck-optimal biconnected subgraph
biconnected_subgraph, bottleneck_weight = construct_biconnected_subgraph(dist_matrix)

# Step 2: Find a tour in the biconnected subgraph
tour = find_tour_in_biconnected_subgraph(biconnected_subgraph, len(coords))

# Calculate tour costs
total_cost, max_distance = calculate_tour_costs(tour, dist_matrix)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")