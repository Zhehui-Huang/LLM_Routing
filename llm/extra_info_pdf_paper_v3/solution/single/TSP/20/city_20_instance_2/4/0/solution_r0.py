import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from itertools import combinations
import networkx as nx

# Coordinate data for cities
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of cities including the depot
n = len(coords)

# Compute the distance matrix
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean(coords[i], coords[j])

# Create and compute the Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(csr_matrix(distance_matrix))
mst_matrix = mst_matrix.toarray().astype(float)

# Adding the transpose because minimum_spanning_tree returns only one direction
mst_matrix += mst_matrix.T

# Find nodes with odd degree in the MST to perform minimum-weight perfect matching
degrees = mst_matrix.sum(axis=0) % 2
odd_degree_nodes = np.where(degrees > 0)[0]

# Generate the subgraph of nodes with odd degree
odd_degree_subgraph = distance_matrix[np.ix_(odd_degree_nodes, odd_degree_nodes)]

# Perfect matching in the subgraph of odd-degree vertices
graph_odd = nx.Graph()
for i in range(len(odd_degree_nodes)):
    for j in range(i + 1, len(odd_degree_nodes)):
        graph_odd.add_edge(odd_degree_nodes[i], odd_degree_nodes[j], weight=odd_degree_subgraph[i][j])

matching = nx.algorithms.matching.min_weight_matching(graph_odd, maxcardinality=True)

# Add matching edges to MST
for x, y in matching:
    mst_matrix[x][y] = distance_matrix[x][y]
    mst_matrix[y][x] = distance_long[x][y]

# Form an Eulerian circuit
mst_graph = nx.Graph(mt_matrix)
eulerian_circuit = list(nx.eulerian_circuit(mst_graph, source=0))

# Convert Eulerian circuit to Hamiltonian path (shortcutting)
visited = set()
hamiltonian_circuit = []

for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # Return to the depot

# Calculate total travel cost
total_cost = 0
for i in range(1, len(hamiltonian_circuit)):
    total_cost += distance_matrix[hamiltonian_circuit[i - 1]][hamiltonian_circuit[i]]

# Output the result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")