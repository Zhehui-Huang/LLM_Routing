import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Define city coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate the Euclidean Distance Matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Create a graph and compute Minimum Spanning Tree (MST)
G = nx.Graph()
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with odd degree in MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Compute Minimum Weight Perfect Matching for odd degree vertices
odd_graph = nx.Graph()
odd_graph.add_nodes_from(odd_degree_nodes)
for u, v in combinations(odd_degree_nodes, 2):
    odd_graph.add_edge(u, v, weight=dist_matrix[u][v])

matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Combine the edges of MST and matching to form a multigraph H
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(matching)

# Find an Eulerian circuit in the multigraph H
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # return to the depot city

# Calculate the total travel cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)