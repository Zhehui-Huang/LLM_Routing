import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Define coordinates for each city, including the depot city 0.
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate the Euclidean distance matrix.
dist = distance_matrix(coords, coords)

# Create a complete graph with the computed distances between each pair of nodes.
G = nx.complete_graph(len(coords))
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        G[i][j]['weight'] = dist[i][j]

# Compute the Minimum Spanning Tree (MST) of the graph.
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices of the graph with an odd degree.
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

# Create the subgraph consisting only of these odd-degree nodes.
odd_subgraph = G.subgraph(odd_degree_nodes)

# Find a minimum weight perfect matching for the subgraph.
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Create an Eulierian multigraph by combining the MST and the perfect matching.
multigraph = nx.MultiGraph(mst)
multigraph.add_edges_from(matching)

# Find an Eulerian circuit in the multigraph.
eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))

# Convert the Eulerian circuit to a Hamiltonian circuit by skipping repeated nodes.
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Calculate the total travel cost for the Hamiltonian circuit.
total_cost = sum(dist[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the results.
print("Tour: ", hamiltonian_circuit)
print("Total travel cost: ", total_cost)