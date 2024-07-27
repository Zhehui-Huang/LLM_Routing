import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_btsp_tour(cities):
    n = len(cities)
    distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    edges = [(i, j, distances[i][j]) for i in range(n) for j in range(i + 1, n)]
    edges.sort(key=lambda x: x[2])  # Sort edges based on distance

    # Find the smallest edge that can still form a Hamiltonian cycle.
    for threshold in range(len(edges)):
        max_edge = edges[threshold][2]
        graph = {i: [] for i in range(n)}
        for i, j, d in edges:
            if d <= max_edge:
                graph[i].append(j)
                graph[j].append(i)

        # Attempt to find any Hamiltonian cycle with the current graph edges.
        for start in range(n):
            tour = [start]
            if dfs(start, graph, set(), tour, n):
                tour.append(start)  # Complete the cycle by returning to the depot
                total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
                return tour, total_cost, max_edge

    return None, None, None

def dfs(node, graph, visited, path, n):
    if len(path) == n:
        return path[0] in graph[node]
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            path.append(neighbor)
            if dfs(neighbor, graph, visited, path, n):
                return True
            path.pop()
            visited.remove(neighbor)
    return False

# Coordinates of cities (depot city included)
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
          (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
          (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
          (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Finding the BTSP tour
tour, total_cost, max_distance = find_btstate_plotsp_tourney(cities)

if tour is not None:
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No valid tour found that satisfies the conditions.")