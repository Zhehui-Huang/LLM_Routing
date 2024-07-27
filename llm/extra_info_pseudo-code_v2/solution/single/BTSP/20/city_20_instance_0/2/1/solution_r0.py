import math
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_biconnected(graph, n):
    _, labels = connected_components(csr_matrix(graph), connection='strong')
    return len(set(labels)) == 1 and all(sum(1 for i in row if i > 0) >= 2 for row in graph)

def compute_bb_graph(coords):
    n = len(coords)
    sorted_edges = []
    graph = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            distance = euclidean_distance(coords[i], coords[j])
            sorted_edges.append((distance, i, j))
    
    sorted_edges.sort()
    bb_graph = [[0]*n for _ in range(n)]
    
    for dist, i, j in sorted_edges:
        bb_graph[i][j] = bb_graph[j][i] = dist
        if is_biconnected(bb_graph, n):
            return bb_graph
        bb_graph[i][j] = bb_graph[j][i] = 0

    return bb_graph

def find_tour(bb_graph):
    n = len(bb_graph)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    current = 0
    
    while len(tour) < n:
        next_city = None
        min_dist = float('inf')
        for j in range(n):
            if not visited[j] and 0 < bb_graph[current][j] < min_dist:
                min_dist = bb_graph[current][j]
                next_city = j
        tour.append(next_city)
        visited[next_city] = True
        current = next_city
    
    tour.append(0)  # return to the depot
    return tour

def evaluate_tour(tour, coords):
    max_distance = 0
    total_cost = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coords[tour[i]], coords[tour[i+1]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    return tour, total_cost, max_distance

# Define the coordinates of each city including the depot
city_coords = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Step 1: Compute the Bottleneck-optimal Biconnected Subgraph (BB graph)
bb_graph = compute_bb_graph(city_coords)

# Step 2: Identify the tour in BB graph
tour = find_tour(bb_graph)

# Evaluate the tour
result_tour, result_total_cost, result_max_distance = evaluate_tour(tour, city_coords)

# Output the result
print(f"Tour: {result_tour}")
print(f"Total travel cost: {result_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {result_max_distance:.2f}")