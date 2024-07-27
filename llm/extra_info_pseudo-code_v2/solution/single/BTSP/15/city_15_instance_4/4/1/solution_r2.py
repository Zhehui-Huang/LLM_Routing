import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

def biconnected_subgraph(dist_matrix):
    n = len(dist_matrix)
    edges = sorted(((dist_matrix[i][j], i, j) for i in range(n) for j in range(i+1, n)), key=lambda x: x[0])
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX

    graph = [[0] * n for _ in range(n)]
    for weight, u, v in edges:
        graph[u][v] = graph[v][u] = weight
        union(u, v)
        # Check biconnectivity using the number of unique parents/root representatives
        if len(set(find(x) for x in range(n))) == 1:
            return graph

def find_tour(graph, start=0):
    # Minimum spanning tree based TSP approximation
    n = len(graph)
    visited = [False] * n
    tour = []
    def visit(node):
        visited[node] = True
        tour.append(node)
        for i in range(n):
            if graph[node][i] != 0 and not visited[i]:
                visit(i)
        if len(tour) < n or node == start:
            tour.append(start)

    visit(start)
    return tour, max(graph[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Define cities and their positions
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate the distances matrix
dist_matrix = create_distance_matrix(cities)

# Get biconnected subgraph
graph = biconnected_subgraph(dist_matrix)

# Finding the tour starting from the depot
tour, max_distance_between_cities = find_tour(graph)

# Calculate total travel cost
total_travel_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_between_cities)