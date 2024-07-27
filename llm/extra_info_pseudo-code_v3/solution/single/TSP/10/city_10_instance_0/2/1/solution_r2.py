import numpy as  np
import networkx as nx
import itertools
from scipy.spatial import distance_matrix

# Coordinates of the cities
coordinates = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Compute Euclidean distances between each pair of points
dist_matrix = distance_matrix(coordinates, coordinates)

# Create a complete graph from the distance matrix
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute the minimum spanning tree T
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree in T
odd_degree_nodes = [node for node, degree in T.degree() if degree % 2 == 1]

# Step 3: Minimum-weight perfect matching M on the subgraph induced by odd degree nodes
M = nx.Graph()
M.add_nodes_from(odd_degree_nodes)
for u, v in itertools.combinations(odd_degree_nodes, 2):
    M.add_edge(u, v, weight=dist_matrix[u][v])

min_weight_matching = nx.algorithms.matching.min_weight_matching(M, maxcardinality=True, weight='weight')

# Step 4: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert Eulerian circuit to a Hamiltonian circuit
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
    visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Return to the starting node

# Total cost calculation
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Printing the tour and total cost
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")