import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from networkx import Graph, eulerian_circuit
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

# Compute the Minimum Spanning Tree
mst_matrix = minimum_spanning_tree(dist_matrix).toarray()

# Helper function to convert MST matrix to Edge List
def mst_to_edges(mst_matrix):
    edges = []
    for i in range(n):
        for j in range(n):
            if mst_matrix[i][j] != 0:
                edges.append((i, j, mst_matrix[i][j]))
    return edges

# MST Edge list
mst_edges = mst_to_edges(mst_matrix)

# Graph for MST
mst_graph = Graph()
mst_graph.add_weighted_edges_from(mst_edges)

# Find odd degree vertices
odd_degree_nodes = [v for v, d in mst_graph.degree() if d % 2 == 1]

# Subgraph of vertices with odd degree
odd_graph = Graph()
odd_graph.add_nodes_from(odd_degree_nodes)

# Add edges between odd degree vertices with weights as distances
for u, v in combinations(odd_degree_nodes, 2):
    odd_graph.add_edge(u, v, weight=dist_matrix[u][v])

# Minimum weight perfect matching
matching = max_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add matching to the MST to form a multigraph
multigraph = Graph(mst_graph)
multigraph.add_edges_from(matching)

# Find an Eulerian circuit
euler_circuit = list(eulerian_circuit(multigraph, source=0))

# Convert the Eulerian circuit to a Hamiltonian path
seen = set()
hamiltonian_circuit = [0]
total_cost = 0
for u, v in euler_circuit:
    if v not in seen:
        seen.add(v)
        hamiltonian_circuit.append(v)
        total_cost += dist_matrix[u][v]

# Since hamiltonian_circuit does not necessarily end at starting point, add manually
hamiltonian_circuit.append(0)
total_cost += dist_audio[hamiltonian_circuit[-2]][0]

# Output result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)