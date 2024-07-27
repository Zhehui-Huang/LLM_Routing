import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_matrix(coords):
    n = len(coords)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return dist_matrix

def find_components(parents):
    # To find connected components via a simple union-find
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parents[rootY] = rootX
    
    return find, union

def is_biconnected(graph, n):
    visited = [False] * n
    disc = [float('Inf')] * n
    low = [float('Inf')] * n
    parent = [-1] * n
    ap = [False] * n
    time = [0]

    def dfs(u):
        nonlocal time
        children = 0
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in range(n):
            if graph[u][v] != 0:  # There is an edge
                if not visited[v]:
                    parent[v] = u
                    children += 1
                    dfs(v)

                    # Check if the subtree rooted at v has a connection back to one of ancestors of u
                    low[u] = min(low[u], low[v])

                    # (1) u is root of DFS tree and has two or more children.
                    if parent[u] == -1 and children > 1:
                        ap[u] = True

                    # (2) If u is not root and low value of one of its child is more than discovery value of u.
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                elif v != parent[u]:  # Update low value of u for parent function calls.
                    low[u] = min(low[u], disc[v])

    for i in range(n):
        if not visited[i]:
            dfs(i)
            if any(visited) and any(not v for v in visited):
                return False  # Not connected
    return not any(ap)

def construct_biconnected_subgraph(dist_matrix):
    n = len(dist_matrix)
    edges = sorted(((i, j, dist_matrix[i][j]) for i in range(n) for j in range(i+1, n)), key=lambda x: x[2])

    graph = [[0] * n for _ in range(n)]
    for u, v, d in edges:
        graph[u][v] = graph[v][u] = d
        if is_biconnected(graph, n):
            return graph, d
        graph[u][v] = graph[v][u] = 0  # This edge does not help in forming a biconnected graph
    return None, None  # Trigger error or exceptional case if biconnected graph not found

def find_tour_in_biconnected_subgraph(graph, n):
    tour = []
    visited = [False] * n

    def dfs(current):
        visited[current] = True
        tour.append(current)
        for neighbor in range(n):
            if graph[current][neighbor] != 0 and not visited[neighbor]:
                dfs(neighbor)

    dfs(0)
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

dist_matrix = create_distance_matrix(coords)
biconnected_subgraph, bottleneck_weight = construct_biconnected_subgraph(dist_matrix)
if biconnected_subgraph:
    tour = find_tour_in_biconnected_subgraph(biconnected_subgraph, len(coords))
    total_cost, max_distance = calculate_tour_costs(tour, dist_matrix)
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("Failed to construct a biconnected subgraph, check city coordinates or method logic.")