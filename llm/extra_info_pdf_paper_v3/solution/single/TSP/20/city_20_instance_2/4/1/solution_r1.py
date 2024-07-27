import math
import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

# Define the cities coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14),
    (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate the Euclidean distance matrix
dist_matrix = distance_matrix(cities, cities)

# Construct the Minimum Spanning Tree using Kruskal's algorithm (using NetworkX for simplicity)
G = nx.Graph()
for i in range(len(dist_matrix)):
    for j in range(i + 1, len(dist_matrix)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

mst_tree = list(nx.minimum_spanning_tree(G).edges(data=True))

# Create the MST graph
mst_graph = nx.Graph()
mst_graph.add_weighted_edges_from((u, v, d['weight']) for u, v, d in mst_tree)

# Determine nodes with odd degree in the MST
odd_degree_nodes = [node for node in mst_graph.nodes if mst_graph.degree(node) % 2 == 1]
odd_graph = nx.Graph()
odd_graph.add_weighted_edges_from((u, v, dist_matrix[u][v]) for u in odd_degree_nodes for v in odd_degree_nodes if u != v)

# Minimum-Cost Perfect Matching on the odd-degree-subgraph
min_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')
mst_graph.add_edges_from(min_matching)

# Create an Eulerian circuit from the graph with added matching edges
eulerian_circuit = list(nx.eulerian_circuit(mst_graph, source=0))

# Convert Eulerian circuit to Hamiltonian path (visiting each node exactly once)
visited = set()
hamiltonian_path = [0]

for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_path.append(v)
        visited.add(v)

# Close the circuit by returning to the depot
hamiltonian_path.append(0)

# Calculate the travel cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[hamiltonian_path[i]][hamiltonian_path[i+1]] for i in range(len(hamiltonian_path) - 1))

# Print the results
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)