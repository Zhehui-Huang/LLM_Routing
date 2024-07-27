import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations
import networkx as nx

# City coordinates
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

# Calculate Euclidean distances between every pair of cities
def calculate_distances(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

dist_matrix = calculate_distances(coordinates)

# Finding a tour using the Christofides algorithm, suitable for TSP, adapted to minimize the bottleneck
def christofides(dist_matrix):
    G = nx.from_numpy_matrix(dist_matrix)
    # Minimum Spanning Tree
    MST = nx.minimum_spanning_tree(G)
    # Minimum weight matching on the odd degree vertices
    odd_vertex_indices = [v for v, degree in MST.degree() if degree % 2 == 1]
    min_weight_matching = nx.Graph()
    min_weight_matching.add_nodes_from(odd_vertex_indices)
    for u, v in combinations(odd_vertex_libs(n), 2):
        min_weight_matching.add_edge(u, v, weight=dist_matrix[u][v])
    matching = list(nx.algorithms.matching.min_weight_matching(min_weight_matching, maxcardinality=True))
    MST.add_edges_from(matching)
    
    eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))
    # Convert to a tour by skipping repeated nodes
    tour = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            tour.append(u)
            visited.add(u)
    tour.append(0)  # return to start
    return tour

tour = christofides(dist_matrix)

# Calculate tour cost and maximum distance
def calculate_tour_costs(tour, dist_matrix):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = dist_matrix[tour[i]][tour[i+1]]
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

total_cost, max_distance = calculate_tour_costs(tour, dist_matrix)

# Outputs
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)