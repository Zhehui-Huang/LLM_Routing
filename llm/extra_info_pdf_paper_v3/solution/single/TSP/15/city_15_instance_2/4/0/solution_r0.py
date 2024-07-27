import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations

# Define the coordinates of each city
coordinates = [
    (54, 87),  # Depot city 0
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)   # City 14
]

# Compute the distance matrix
num_cities = len(coordinates)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = euclidean(coordinates[i], coordinates[j])

# Helper function to find a MST using Prim's Algorithm
def minimum_spanning_tree(dist_matrix):
    num_vertices = dist_matrix.shape[0]
    in_mst = np.zeros(num_vertices, dtype=bool)
    min_edge = np.full(num_vertices, np.inf)
    parent = np.full(num_vertices, -1, dtype=int)
    min_edge[0] = 0  # Start from vertex 0
    total_cost = 0

    for _ in range(num_vertices):
        u = np.argmin(min_edge)
        in_mst[u] = True
        total_cost += min_edge[u]
        min_edge[u] = np.inf

        for v in range(num_vertices):
            if not in_mst[v] and dist_matrix[u][v] < min_edge[v]:
                min_edge[v] = dist_matrix[u][v]
                parent[v] = u

    return parent, total_cost

# Function to find vertices of odd degree in the Minimum Spanning Tree
def find_odd_vertices(parent):
    degree = np.zeros(len(parent), dtype=int)
    for p in parent:
        if p != -1:
            degree[p] += 1
            degree[np.where(parent == p)[0]] += 1
    return np.where(degree % 2 == 1)[0]

# Minimum weight perfect matching using a simple greedy approach (not optimal)
def minimum_weight_matching(odd_vertices, dist_matrix):
    matched = np.zeros(dist_matrix.shape[0], dtype=bool)
    matching_edges = []
    
    while not all(matched[odd_vertices]):
        min_edge = np.inf
        x, y = -1, -1
        for u in odd_vertices:
            if matched[u]:
                continue
            for v in odd_vertices:
                if u != v and not matched[v] and dist_matrix[u][v] < min_edge:
                    min_edge = dist_format_matrix[u][v]
                    x, y = u, v
        matched[x] = matched[y] = True
        matching_edges.append((x, y))
    return matching_edges

# Function to convert a MST to a tour
def create_tour(parent, num_vertices):
    tour = []
    visited = np.zeros(num_vertices, dtype=bool)

    def visit(vertex):
        visited[vertex] = True
        tour.append(vertex)
        for i in range(num_vertices):
            if parent[i] == vertex or parent[vertex] == i:
                if not visited[i]:
                    visit(i)
                    tour.append(vertex)

    visit(0)  # Start the tour at the depot city
    tour.append(0)  # Return to the depot city at the end
    return tour

# Calculating the Minimum Spanning Tree
mst_parent, _ = minimum_spanning_tree(dist_matrix)
odd_vertices = find_odd_vertices(mst_parent)
matching_edges = minimum_weight_matching(odd_vertices, dist_matrix)

# Creating Eulerian circuit by combining MST and matching edges
tour = create_tour(mst_parent, num_cities)

# Calculate the total travel cost of the tour
total_travel_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_pulse:.2f}")