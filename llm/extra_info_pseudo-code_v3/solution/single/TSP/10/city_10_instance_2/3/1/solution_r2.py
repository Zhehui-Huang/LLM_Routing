import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix

# Provided coordinates of cities and the depot
coordinates = np.array([
    (90, 3), (11, 17), (7, 27), (95, 81), (41, 54),
    (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
])

# Compute the distance matrix (Euclidean distances)
dist_matrix = distance_matrix(coordinates, coordinates)

# Construct a complete graph with distance weights
G = nx.Graph()
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Compute a Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# Identify vertices with odd degree in MST
odd_degree_nodes = [node for node, degree in T.degree() if degree % 2 == 1]

# Subgraph induced by odd-degree nodes
odd_subgraph = G.subgraph(odd_degree_nodes)

# Find minimum weight perfect matching in the subgraph
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Add the matched edges to the MST to create a new graph
T.add_edges_from(min_weight_matching)

# Find an Eulerian circuit in T
eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

# Create the Hamiltonian circuit by skipping visited nodes
visited = set()
hamiltonian_circuit = []
for u, _ in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # append start/end node

# Calculate the total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Printing the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(total_cost, 2))