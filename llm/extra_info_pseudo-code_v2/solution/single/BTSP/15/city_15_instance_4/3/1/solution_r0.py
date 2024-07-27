import math
import itertools
from collections import defaultdict

cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), 
          (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), 
          (53, 80), (21, 21), (12, 39)]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute all pairs of distances
distances = {}
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        distance = euclidean_distance(cities[i], cities[j])
        distances[(i, j)] = distance
        distances[(j, i)] = distance

def is_biconnected(graph_edges):
    def dfs(vertex, parent):
        nonlocal count
        visited[vertex] = True
        discovery[vertex] = low[vertex] = count
        count += 1
        children = 0
        
        for v in graph_edges[vertex]:
            if not visited[v]:
                parent[v] = vertex
                children += 1
                dfs(v, parent)
                # Check if the subtree rooted at v has a connection back to one of the ancestors of u
                low[vertex] = min(low[vertex], low[v])
                
                # No back edge found, it's an articulation point
                if parent[vertex] == -1 and children > 1:
                    return False
            elif v != parent[vertex]:
                low[vertex] = min(low[vertex], discovery[v])
                
        return True

    n = len(cities)
    visited = [False] * n
    discovery = [0] * n
    low = [0] * n
    parent = [-1] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            if not dfs(i, parent):
                return False
    return True

def find_bottleneck_tour():
    # Step 0: Initialize
    sorted_edges = sorted(distances.items(), key=lambda x: x[1])
    graph_edges = defaultdict(list)
    edges_in_solution = []

    # Step 1: Augmentation
    for (i, j), dist in sorted_edges:
        graph_edges[i].append(j)
        graph_edges[j].append(i)
        edges_in_solution.append((i, j))
        # Step 2: Check if biconnected
        if is_biconnected(graph_edges):
            last_distance = dist
            break
    
    # Get the tour from the biconnected subgraph
    # Here we use a simple nearest neighbour approach for tour construction as a placeholder
    tour = [0]
    visited = [False] * len(cities)
    visited[0] = True
    current_city = 0
    for _ in range(len(cities) - 1):
        next_city = min((j for j in range(len(cities)) if not visited[j]), key=lambda x: distances[(current_city, x)])
        tour.append(next_city)
        visited[next_city] = True
        current_city = next_city
    tour.append(0)  # return to depot city

    # Calculate total cost and max distance in tour
    total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    max_distance = max(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

    return tour, total_cost, max_distance

tour, total_cost, max_distance = find_bottleneck_tour()

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)