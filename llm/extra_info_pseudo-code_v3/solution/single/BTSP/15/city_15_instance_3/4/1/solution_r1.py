import math
from itertools import combinations

def calc_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def construct_graph(cities):
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = calc_euclidean_distance(cities[i], cities[j])
            distances[i][j] = distances[j][i] = dist
    return distances

def hamiltonian_path_exists(n, graph, src):
    """ Check if there exists a Hamiltonian path using backtracking DFS. """
    def dfs(node, count, visited):
        if count == n:
            return True
        visited.add(node)
        for neighbor in range(n):
            if neighbor not in visited and graph[node][neighbor]:
                if dfs(neighbor, count + 1, visited):
                    return True
        visited.remove(node)
        return False
    
    visited = set()
    return dfs(src, 1, visited)

def bottleneck_tsp(cities):
    distances = construct_graph(cities)
    n = len(cities)
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    edges.sort(key=lambda x: distances[x[0]][x[1]])
    
    best_path = None
    best_total_cost = float('inf')
    best_max_distance = float('inf')
    
    for edge_index in range(len(edges)):
        max_edge_weight = distances[edges[edge_index][0]][edges[edge_index][1]]
        graph = [[False]*n for _ in range(n)]
        for i, j in edges[:edge_total+1]:
            graph[i][j] = graph[j][i] = distances[i][j] <= max_edge_weight
            
        if hamiltonian_path_exists(n, graph, 0):
            total_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path)-1))
            if total_cost < best_total_cost:
                best_total_cost = total_cost
                best_max_distance = max_edge_weight
                best_path = path
    
    return best_path, best_total_cost, best_max_distance

# Cities coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Solve Bottleneck TSP
tour, total_cost, max_distance = bottleneck_tsp(cities)

# Output results
if tour:
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
    print("Maximum distance between consecutive cities:", round(max_distance, 2))
else:
    print("No valid tour found.")