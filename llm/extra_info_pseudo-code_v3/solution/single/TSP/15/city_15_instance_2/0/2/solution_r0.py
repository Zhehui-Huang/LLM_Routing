import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
import itertools

# City coordinates
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Calculate Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Create complete graph
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute a minimum spanning tree (MST) of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify vertices with odd degree in T
odd_degree_vertices = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Find minimum weight perfect matching in the subgraph induced by vertices with odd degree
subgraph = G.subgraph(odd_degree_vertices)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of T and M to form a multigraph
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited or v == 0:  # allow revisiting the depot only
        visited.add(v)
        hamiltonian_circuit.append(v)

# Ensure the tour ends at the depot
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate the total travel cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)