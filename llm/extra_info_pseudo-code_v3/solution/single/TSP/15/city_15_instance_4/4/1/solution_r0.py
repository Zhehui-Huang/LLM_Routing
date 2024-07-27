import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# City coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Compute the pairwise Euclidean distance matrix
dist_matrix = distance_matrix(cities, cities)

# Create a complete graph with 15 nodes
G = nx.complete_graph(len(cities))

# Set the weight for the edges based on the distance matrix
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute a minimum spanning tree (MST) of G
T = nx.minimum_spanning_tree(G)

# Step 2: Identify vertices with odd degree in T
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Find minimum weight perfect matching in the subgraph induced by odd_degree_nodes
subgraph = G.subgraph(odd_degree_node)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)

# Adding start point to complete the circuit
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the total travel cost
total_travel_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output the tour and total travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel # Output the results