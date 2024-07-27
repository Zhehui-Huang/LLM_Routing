import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist
from itertools import combinations

# City coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate the distance matrix
dist_matrix = cdist(cities, cities)

# Create a complete graph with weights from the distance matrix
G = nx.complete_graph(len(cities))
for i in range(G.number_of_nodes()):
    for j in range(i+1, G.number_of_nodes()):
        G[i][j]['weight'] = dist_matrix[i][j]

# Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G)

# Find vertices with odd degree in T
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Create subgraph of nodes with odd degree
subgraph = G.subgraph(odd_degree_nodes)

# Find minimum weight perfect matching for odd degree nodes
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add the matching edges to the tree
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Convert the Eulerian circuit to a Hamiltonian circuit (path), removing duplicates
visited = set()
hamiltonian_circuit = [0]  # include depot city as the start and end point
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)  # ensure returning to the depot city

# Calculate the total travel cost
total_travel_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit)-1))

# Print the output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)