import math
from itertools import combinations
from scipy.spatial.distance import pdist, squareform
import networkx as nx

# Given city coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48),
}

# Create a distance matrix using Euclidean distance
coords = list(cities.values())
dist_matrix = squareform(pdist(coords))

# Create a graph from the distance matrix
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Find Minimum Spanning Tree
MST = nx.minimum_spanning_tree(G)

# Find vertices of odd degree in MST
odd_degree_nodes = [node for node, degree in MST.degree() if degree % 2 == 1]

# Minimum Weight Perfect Matching on the induced subgraph of G containing odd degree vertices
odd_graph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Add matching edges to MST
MST.add_edges_from(min_weight_matching)

# Find Eulerian Circuit
eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))

# Convert Eulerian circuit to Hamiltonian circuit (shortcutting)
visited = set()
tour = []
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)

# Add starting point to end to complete the tour
tour.append(0)

# Calculate total travel cost of the tour
tour_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

output = {
    "Tour": tour,
    "Total travel cost": tour_cost
}

output