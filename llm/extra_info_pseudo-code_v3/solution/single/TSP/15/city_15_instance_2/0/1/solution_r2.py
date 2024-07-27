import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

# Define coordinates of cities including the depot
coordinates = np.array([
    (54, 87),  # Depot
    (21, 84), (69, 84), (53, 40),
    (54, 42), (36, 30), (52, 82), (93, 44),
    (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
])

# Compute Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Create a complete graph with the distances as the weights
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(i, len(coordinates)):
        G[i][j]['weight'] = dist_matrix[i][j]
        G[j][i]['weight'] = dist_matrix[i][j]  # Ensure symmetry

# Step 1: Compute a minimum spanning tree (MST) of G
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices with odd degree in T
odd_degree_nodes = [node for node in mst.nodes() if mst.degree(node) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(mst)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # back to the starting node (depot)

# Calculate the total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)