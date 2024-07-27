import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Input coordinates of cities
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Convert city coords to an array
coords = np.array(list(cities.values()))

# Compute pairwise Euclidean distances
dist_matrix = distance_matrix(coords, coords)

# Create a complete graph from the distance matrix
G = nx.complete_graph(len(cities))
for i, j in combinations(cities, 2):
    G.add_edge(i, j, weight=dist_matrix[i][j])

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with an odd degree in the MST
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 == 1]

# Subgraph of G induced by odd degree nodes
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add the minimum weight matching edges to the MST
mst.add_edges_from(min_weight_matching)

# Form Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Making it a Hamiltonian circuit by skipping visited nodes (shortcutting)
visited = set()
tour = []
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
    if v not in visited:
        tour.append(v)
        visited.add(v)

# Ensure to end at the starting point (depot city)
tour.append(tour[0])

# Calculate total travel cost
total_travel_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")