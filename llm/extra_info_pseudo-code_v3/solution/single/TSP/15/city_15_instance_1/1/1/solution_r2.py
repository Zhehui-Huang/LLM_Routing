import numpy as np
import networkx as nx
from itertools import combinations
from scipy.spatial.distance import pdist, squareform

# Coordinates of cities including the depot
cities_coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Compute pairwise Euclidean distance matrix
dist_matrix = squareform(pdist(cities_coordinates))

# Number of cities
n = len(cities_coordinates)

# Create complete graph from distance matrix
G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Step 1: Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Vertices of odd degree
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 != 0]

# Step 3: Minimum Weight Perfect Matching on the subgraph induced by odd degree vertices
odd_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of the MST and the matching to make an Eulerian graph
mst.add_edges_from(min_weight_matching)

# Step 5: Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Making it a Hamiltonian circuit by skipping visited vertices (shortcutting)
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Return to the start to complete the circuit
hamiltonian_circuit.append(0)

# Calculate the total cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel trip cost:", total_cost)