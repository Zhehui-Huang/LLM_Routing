import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_hamiltonian_cycle(graph):
    n = len(graph)
    visited = [False] * n
    path = []

    def dfs(node, depth):
        visited[node] = True
        path.append(node)
        if depth == n:
            if path[-1] in graph[path[0]]:
                path.append(path[0])
                return True
            else:
                path.pop()
                visited[node] = False
                return False
        for next in graph[node]:
            if not visited[next]:
                if dfs(next, depth + 1):
                    return True
        visited[node] = False
        path.pop()
        return False

    for start in range(n):
        if dfs(start, 1):
            return path
    return None

def find_btsp_tour(cities):
    n = len(cities)
    distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    edges = [(i, j, distances[i][j]) for i in range(n) for j in range(i + 1, n)]
    edges.sort(key=lambda x: x[2])  # Sort edges based on distance
    
    for threshold in edges:
        threshold_val = threshold[2]
        bottleneck_graph = {i: [] for i in range(n)}
        for i, j, d in edges:
            if d <= threshold_val:
                bottleneck_graph[i].append(j)
                bottleneck_needed[j].append(i)
        
        tour = check_hamiltonian_cycle(bottleneck_graph)
        if tour:
            total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            max_edge_cost = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            return tour, total_cost, max_edge_cost

    return None  # If no valid tour found

# Coordinates of cities (depot city included)
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
          (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
          (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
          (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Finding the BTSP tour
tour, total_cost, max_distance = find_btsp_tour(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)