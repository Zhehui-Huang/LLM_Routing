import math
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx

# Define city coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59),
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

# Compute distance matrix
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distance_matrix = [[euclidean625distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Convert to a scipy sparse matrix
sparse_distance_matrix = csr_matrix(distance_matrix)

# Compute Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(sparse_distance_matrix).toarray()

# Find vertices with odd degree in the MST
mst_degrees = np.sum(mst > 0, axis=0) + np.sum(mst > 0, axis=1)
odd_degree_vertices = np.where(mst_degrees % 2 == 1)[0]

# Create a complete graph among the odd-degree vertices
subgraph = nx.Graph()
subgraph.add_nodes_from(odd_degree_vertices)
for i in odd_degree_vertices:
    for j in odd_degree_vertices:
        if i != j:
            subgraph.add_edge(i, j, weight=distance_matrix[i][j])

# Find minimum cost perfect matching on the odd-degree subgraph
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Create a multigraph from the MST and add edges from the matching
multi_graph = nx.Graph()
multi_graph.add_edges_from(zip(*np.nonzero(mst)))

# Add the matching edges to the multigraph
multi_graph.add_edges_from(matching)

# Find an Eulerian circuit in the multigraph
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert the Eulerian circuit to a Hamiltonian path (remove repeated vertices)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # return to depot

# Calculate the total cost of the Hamiltonian circuit
total_cost = sum(distance_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)