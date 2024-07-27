import numpy as np
import networkx as nx
from itertools import combinations
from scipy.spatial import distance_matrix

# Define cities coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Compute distance matrix
points = np.array(list(cities.values()))
distMatrix = distance_matrix(points, points)

# Create complete graph
G = nx.complete_graph(len(cities))
for i in range(len(points)):
    for j in range(len(points)):
        G[i][j]['weight'] = distMatrix[i][j]

# Step 1: Minimum Spanning Tree
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degrees
odds = [x for x in T.nodes() if T.degree(x) % 2 == 1]

# Step 3: Minimum weight perfect matching on odd degree vertices
odd_subgraph = G.subgraph(odds)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Add matching edges to the tree
T.add_edges_from(min_weight_matching)

# Step 4 and 5: Create multigraph and find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

# Step 6: Create a Hamiltonian circuit by skipping visited nodes
circuit, visited = [], set()
for u, v in eulerian_circuit:
    if u not in visited:
        circuit.append(u)
        visited.add(u)
circuit.append(circuit[0])  # to form a cycle back to the starting node

# Calculate the total cost of the Hamiltonian Circuit
total_cost = sum(G[u][v]['weight'] for u, v in zip(circuit[:-1], circuit[1:]))

# Print results
print("Tour:", circuit)
print("Total travel cost:", total_cost)