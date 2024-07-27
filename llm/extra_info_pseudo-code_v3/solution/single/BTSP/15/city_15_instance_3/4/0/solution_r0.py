import math
import itertools
import sys

# Declaration of cities using tuples (x, y)
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), 
          (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Create a graph based on a distance threshold
def create_bottleneck_graph(threshold):
    n = len(cities)
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if euclidean_distance(i, j) <= threshold:
                graph[i].append(j)
                graph[j].append(i)
    return graph

# Helper function to check if all nodes are connected in any thresholded graph
def is_connected(graph, n):
    visited = [False] * n
    stack = [0]
    cnt = 0
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            cnt += 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    
    return cnt == n

# DFS to find any Hamiltonian path
def hamiltonian_path_exists(graph, start_node, n):
    path = []
    
    def dfs(current, depth, visited):
        if depth == n:
            return True
        visited[current] = True
        path.append(current)
        for neighbor in graph[current]:
            if not visited[neighbor] and dfs(neighbor, depth + 1, visited):
                return True
        visited[current] = False
        path.pop()
        return False

    visited = [False] * n
    return dfs(start_node, 1, visited), path

# Bottleneck TSP algorithm
def bottleneck_tsp():
    edges = []
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(i, j)
            edges.append((dist, i, j))
            
    edges.sort()  # sort edges based on distance
    
    for dist, _, _ in edges:
        graph = create_bottleneck_graph(dist)
        if is_connected(graph, n):
            exists, path = hamiltonian_path_exists(graph, 0, n)
            if exists and len(path) == n:
                path.append(0)  # Complete the cycle
                max_leg = max(euclidean_distance(path[i], path[i + 1]) for i in range(n))
                total_cost = sum(euclidean_distance(path[i], path[i + 1]) for i in range(n))
                return path, total_cost, max_leg

    return None, None, None

# Execute the function
tour, total_travel_cost, max_distance = bottleneck_tsp()

if tour:
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel buddies with the mentioned method={int(math.round(x)) for x, in and between.")
    print(f" Maximum}'ere times off consecutive; youth distance stride.")