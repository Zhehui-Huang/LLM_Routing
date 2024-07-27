import math
from itertools import permutations

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

def find_path(n, graph, max_edge_weight):
    # Use DFS to find a hamiltonian path starting from node 0
    path = []
    visited = [False] * n
    visited[0] = True
    path.append(0)

    def dfs(current):
        if len(path) == n:
            if graph[path[-1]][0] <= max_edge_weight:  # Check if it can return to the start
                path.append(0)  # Complete the cycle
                return True
            else:
                return False
        
        for next_node in range(n):
            if not visited[next_node] and graph[current][next_node] <= max_edge_weight:
                visited[next_node] = True
                path.append(next_node)
                if dfs(next_node):
                    return True
                path.pop()
                visited[next_node] = False
        return False

    if dfs(0):
        return path
    else:
        return None

def bottleneck_tsp(cities):
    distances = construct_graph(cities)
    n = len(cities)
    edge_list = [distances[i][j] for i in range(n) for j in range(i+1, n)]
    sorted_edges = sorted(set(edge_list))

    for max_edge_weight in sorted_edges:
        path = find_path(n, distances, max_edge_weight)
        if path:
            max_distance = max(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
            total_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
            return path, total_cost, max_distance

    return None, None, None

# Provided cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Solve the problem
tour, total_cost, max_dist = bottleneck_tsp(cities)

# Print results
if tour:
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
    print("Maximum distance between consecutive cities:", round(max_dist, 2))
else:
    print("No feasible tour was found.")