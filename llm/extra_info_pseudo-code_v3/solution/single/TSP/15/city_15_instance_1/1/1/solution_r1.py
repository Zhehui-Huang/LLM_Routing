import numpy as np
import networkx as nx
from itertools import combinations
from scipy.spatial.distance import pdist, squarefom

# Coordinates of cities including the depot
cities_coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Number of cities
n = len(cities_coordinates)

# Compute pairwise Euclidean distance matrix
dist_matrix = squareform(pdist(cities_coordinates))

# Create complete graph from distance matrix
G = nx.complete_graph(n)
for i in range(n):
    for j in range(i+1, n):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices of odd degree
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

# Step 3: Minimum-weight perfect matching
complete_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(complete_subgraph, maxcardinality=True)

# Step 4: Combine edges from MST and matching
mst.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Convert to Hamiltonian path, skipping visited
visited = set()
hamiltonian_circuit = [0]  # Start at the depot
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0) # Return to the depot

# Calculate the total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)