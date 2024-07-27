import math
import itertools
from collections import defaultdict

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_biconnected(graph, num_vertices):
    """
    Check if the given graph is biconnected using depth-first search (DFS).
    A graph is biconnected if it has no articulation points (vertices removing which increases number of connected components).
    """
    start_vertex = 0
    discovery = [-1] * num_vertices
    low = [-1] * num_extices
    parent = [-1] * num_vertices
    articulation_points = [False] * num_vertices
    
    def dfs(vertex, discovery, low, parent, articulation_points, time):
        children = 0
        discovery[vertex] = low[vertex] = time
        time += 1
        for neighbor in graph[vertex]:
            if discovery[neighbor] == -1:  # neighbor is not visited
                parent[neighbor] = vertex
                children += 1
                dfs(neighbor, discovery, low, parent, articulation_points, time)
                low[vertex] = min(low[vertex], low[neighbor])

                if parent[vertex] == -1 and children > 1:
                    articulation_points[vertex] = True
                if parent[vertex] != -1 and low[neighbor] >= discovery[vertex]:
                    articulation_points[vertex] = True
            elif neighbor != parent[vertex]:
                low[vertex] = min(low[vertex], discovery[neighbor])

    dfs(start_vertex, discovery, low, parent, articulation_points, 0)
    return not any(articulation_points)

def compute_bottleneck(graph):
    return max(max(edge for edge in subgraph) for subgraph in graph.values())

def optimize_tour_bottleneck(cities):
    num_cities = len(cities)
    edges = []
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            edges.append((i, j, euclidean_distance(cities[i], cities[j])))

    edges.sort(key=lambda x: x[2])  # Sort by distance
    
    parent = list(range(num_cities))
    rank = [0] * num_cities
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
    
    graph = defaultdict(list)
    for i, j, w in edges:
        graph[i].append((j, w))
        graph[j].append((i, w))
        union(i, j)
        if is_biconnected(graph, num_cities):
            break
    
    # Finding a Hamiltonian path (approximate) in the constructed biconnected graph
    visited = [False] * num_cities
    tour = []
    def dfs(current):
        tour.append(current)
        visited[current] = True
        if len(tour) == num_cities:
            return True
        for neighbor, weight in sorted(graph[current], key=lambda x: x[1]):
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
        tour.pop()
        visited[current] = False
        return False
    
    dfs(0)
    tour.append(0)  # Return to the starting city
    
    # Calculate total travel cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    return tour, total_cost, max_distance

# Define city coordinates
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
          (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

tour, total_cost, max_distance = optimize_tour_bottleneck(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)