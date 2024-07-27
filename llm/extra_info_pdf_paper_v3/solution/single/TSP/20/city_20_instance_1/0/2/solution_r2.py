import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# Define the city coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Generate the distance matrix
dist_matrix = np.array([[euclidean(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))])

# Create the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(csr_matrix(dist_matrix))

# Convert the MST to a NetworkX graph
G_mst = nx.from_scipy_sparse_matrix(csr_matrix(mst), edge_attribute='weight')

# Find the set of vertices with odd degree
odd_degree_nodes = [v for v, d in G_mst.degree() if d % 2 != 0]

# Create the subgraph of these nodes and find a minimum weight matching
subgraph = G_mst.subgraph(odd_degree_nodes)
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add the matching edges to the MST
G_mst_augmented = nx.MultiGraph(G_mst)
G_mst_augmented.add_edges_from(matching)

# Find an Eulerian circuit in the MultiGraph
euler_circuit = list(nx.eulerian_circuit(G_mst_augmented, source=0))

# Construct the Hamiltonian circuit by visiting each node exactly once
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Returning to the starting city (depot)

# Compute the travel cost of the Hamiltonian circuit
total_travel_cost = sum([dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1)])

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)