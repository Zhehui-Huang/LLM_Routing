import numpy as np
from scipy.spatial.distance import pdist, squareform
import networkx as nx

# Define city coordinates
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), (61, 16),
    (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

# Compute the distance matrix
dist_matrix = squareform(pdist(coordinates, metric='euclidean'))

# Create a graph from the distance matrix
G = nx.Graph()
for i in range(len(coordinates)):
    for j in range(i+1, len(coordinates)):
        G.add_edge(i, j, weight=dist_cut_matrix[i][j])

# Step 1: Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Step 2: Get vertices with odd degree
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Step 3: Get Minimum Weight Perfect Matching for subgraph induced by odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add the minimum weight perfect matching to the MST
mst.add_edges_from(min_weight_matching)

# Step 4: Find an Eulerian tour
eulerian_tour = list(nx.eulerian_circuit(mst, source=0))

# Step 5 and 6: Convert to Hamiltonian circuit by skipping visited nodes
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_tour:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
if hamiltonian_circuit[-1] != 0:  # Ensure it ends at the depot
    hamiltonian_circuit.append(0)

# Calculate total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Result output
print("Tour: ", hamiltonian_circuit)
print("Total travel cost: {:.2f}".format(total_cost))