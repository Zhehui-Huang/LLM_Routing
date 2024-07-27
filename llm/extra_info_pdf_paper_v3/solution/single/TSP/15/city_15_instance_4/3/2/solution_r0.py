import math
import networkx as nx
from scipy.spatial import distance_matrix
import numpy as np

# Define the coordinates for each city
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Create a distance matrix
coords = np.array(list(cities.values()))
dist_matrix = distance_matrix(coords, coords)

# Build a complete graph
G = nx.complete_graph(len(cities))
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        G.edges[i, j]['weight'] = dist_matrix[i][j]

# Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find vertices of odd degree in MST
odd_degree_nodes = [node for node, degree in mst.degree() if degree % 2 == 1]

# Create a subgraph induced by vertices with odd degree
subgraph = G.subgraph(odd_degree_nodes)

# Minimum weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(subgraph, True)

# Combine the edges of the MST and the matching
for edge in matching:
    mst.add_edge(*edge)

# Find an Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Making a Hamiltonian cycle by shortening the Eulerian circuit
visited = set()
tour = []
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        tour.append(u)
    if v not in visited:
        visited.add(v)
        tour.append(v)

if tour[-1] != 0:
    tour.append(0)

# Calculate the total cost of the tour
total_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)