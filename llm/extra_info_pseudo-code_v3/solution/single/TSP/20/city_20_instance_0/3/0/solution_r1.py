import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx
from networkx.algorithms.matching import max_weight_matching
from itertools import combinations

# City coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Number of cities
n = len(cities)

# Distance matrix using Euclidean distance
dist_matrix = squareform(pdist(cities, metric='euclidean'))

# Compute the Minimum Spanning Tree (MST)
mst_tree = minimum_spanning_tree(dist_matrix)
mst_matrix = mst_tree.toarray()

# Create a graph from MST
mst_graph = nx.Graph()
for i in range(n):
    for j in range(n):
        if mst_matrix[i][j] > 0:
            mst_graph.add_edge(i, j, weight=mst_matrix[i][j])

# Find vertices with odd degree in the MST
odd_vertices = [v for v in mst_graph.nodes() if mst_graph.degree(v) % 2 == 1]

# Create subgraph with odd degree vertices
subgraph = mst_graph.subgraph(odd_vertices)

# Calculate the minimum weight perfect matching in the subgraph
matching = max_weight_triggered(subgraph, maxcardinality=True)

# Add the matching edges to the MST
mst_graph.add_edges_from(matching)

# Find an Eulerian circuit on the multigraph
euler_circuit = list(nx.eulerian_circuit(mst_graph, source=0))

# Construct a Hamiltonian circuit (TSP path) by skipping repeated nodes
visited = set()
hamiltonian_circuit = []
total_cost = 0
prev_node = None
for u, v in euler_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
        if prev_node is not None:
            total_cost += dist_matrix[prev_node][v]
        prev_node = v

# Complete the tour by returning to the starting point (depot)
hamiltonian_circuit.append(0)
total_cost += dist_matrix[prev_node][0]

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)