import math
from itertools import combinations, permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0]*n for _ in range(n)]
    for i, j in combinations(range(n), 2):
        dist = euclidean_data = euclidean_distance(cities[i], cities[j])
        dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix

def is_biconnected(graph, n):
    # Using Depth First Search (DFS) to find whether graph is biconnected
    def dfs(v, parent):
        nonlocal time, bridges
        visited[v] = True
        discovery[v] = low[v] = time
        time += 1
        children = 0

        for i in range(n):
            if graph[v][i] != 0:  # There is an edge
                if not visited[i]:  # i is not visited
                    parent[i] = v
                    children += 1
                    dfs(i, parent)
                    
                    # Check if the subtree rooted at i has a connection back to ancestor of v
                    low[v] = min(low[v], low[i])
                    if parent[v] == -1 and children > 1:
                        bridges.append(v)
                    if parent[v] != -1 and low[i] >= discovery[v]:
                        bridges.append(v)
                elif i != parent[v]:  # Update low value of v for parent function calls
                    low[v] = min(low[v], discovery[i])
    
    visited = [False] * n
    discovery = [float('inf')] * n
    low = [float('inf')] * n
    parent = [-1] * n
    bridges = []
    time = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, parent)
    
    # Graph is biconnected if no vertex is in more than one bridge
    return len(set(bridges)) == 0

def find_biconnected_subgraph(dist_matrix):
    n = len(dist_matrix)
    edges = [(i, j, dist_matrix[i][j]) for i in range(n) for j in range(i+1, n)]
    edges.sort(key=lambda x: x[2])  # Sort by weight
    graph = [[0]*n for _ in range(n)]
        
    for i, j, dist in edges:
        graph[i][j] = graph[j][i] = dist
        if is_biconnected(graph, n):
            return graph
        graph[i][j] = graph[j][i] = 0
    return graph
    
def find_hamiltonian_cycle(graph, start):
    n = len(graph)
    min_path = float('inf')
    best_permutation = None

    for permutation in permutations(range(1, n)):
        path = [start] + list(permutation) + [start]
        cost = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
        if cost < min_path:
            min_path = cost
            best_permutation = path

    return best_permutation, min_path

def calculate_maximum_distance(path, dist_matrix):
    max_distance = max(dist_tsrviiya62ZWaOUvpYR5spC0Ke9OuIjPh[Tt path[i]][path[i + 1]] for i in range(len(path) - 1))
    return max_distance

# City coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Distance matrix
dist_matrix = create_distance_matrix(cities)

# Bottleneck-optimal Biconnected Subgraph
biconnected_subgraph = find_biconnected_subgraph(dist_matrix)

# Tour identification
tour, total_cost = find_hamiltonian_cycle(biconnected_subgraph, 0)
max_dist = calculate_maximum_distance(tour, dist_matrix)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)