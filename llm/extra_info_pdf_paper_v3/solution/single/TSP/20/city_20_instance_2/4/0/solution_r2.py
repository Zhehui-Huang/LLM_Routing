import numpy as np
from scipy.spatial.distance import pdist, squareform
import networkx as nx

# Coordinates for each city including the depot city
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of cities including the depot
n = len(coords)

# Create a distance matrix
dist_matrix = squareform(pdist(coords, metric='euclidean'))

# Create a complete graph from the distance matrix
G = nx.complete_graph(n)
for i in range(n):
    for j in range(i + 1, n):
        G[i][j]['weight'] = dist_matrix[i][j]

# Compute Minimum Spanning Tree (MST) of the graph
T = nx.minimum_spanning_tree(G)

# Find nodes with odd degree in the MST
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Create a subgraph with these odd degree nodes
odd_graph = G.subgraph(odd_degree_nodes)

# Find a minimum weight perfect matching in the subgraph
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Add the edges of this matching to the MST
T.add_edges_from(min_weight_matching)

# Form an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

# Convert Eulerian circuit to Hamiltonian path (shortcutting)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # Close the tour by returning to the depot

# Calculate total travel cost
total_cost = 0
for i in range(1, len(hamiltonian_circuit)):
    total_cost += dist_matrix[hamiltonian_circuit[i - 1]][hamiltonian_circuit[i]]

# Print the result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")