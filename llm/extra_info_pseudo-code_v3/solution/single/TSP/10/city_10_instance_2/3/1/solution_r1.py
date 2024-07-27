import numpy as np
import networkx as nx
from itertools import combinations
from scipy.spatial import distance_matrix

# Provided coordinates of cities and the depot
coordinates = np.array([
    (90, 3), (11, 17), (7, 27), (95, 81), (41, 54), 
    (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
])

# Compute the distance matrix (Euclidean distances)
dist_matrix = distance_matrix(coordinates, coordinates)

# Construct a complete graph with distance weights
G = nx.complete_graph(len(coordinates))
for i, j in G.edges():
    G[i][j]['weight'] = dist_matrix[i][j]

# Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# Identify vertices with odd degree in MST
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Minimum-weight perfect matching in the subgraph induced by odd-degree nodes
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add the matching to MST
T.add_edges_from(min_weight_matching)

# Find an Eulerian circuit in the updated graph (T)
eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

# Convert the Eulerian circuit to a Hamiltonian circuit (skip repeated vertices)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)

# Ensure to add depot city at the end to complete the tour
hamiltonian_circuit.append(0)

# Calculate the total travel cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)