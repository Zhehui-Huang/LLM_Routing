import numpy as np
from scipy.spatial import distance
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# Define the cities' coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Compute the adjacency matrix of distances (Euclidian)
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i][j] = distance.euclidean(cities[i], cities[j])
        else:
            dist_matrix[i][j] = float('inf')

# Convert distance matrix to a minimum spanning tree
mst = minimum_spanning_tree(csr_matrix(dist_matrix))

# Find vertices with odd degree in the MST
graph = nx.from_scipy_sparse_matrix(mst)
odd_degree_nodes = [node for node, degree in dict(graph.degree()).items() if degree % 2 == 1]

# Find the minimum weight perfect matching on odd-degree nodes
subgraph = graph.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Merge MST and Matching to get multigraph H
multigraph = nx.MultiGraph(graph)
multigraph.add_edges_from(min_weight_matching)

# Find an Eulerian Circuit in multigraph H
eulerian_circuit = list(nx.eulerian_circuit(multigraph))

# Convert Eulerian circuit to Hamiltonian circuit, skipping visited nodes
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # returning to the depot

# Calculate the travel cost
total_cost = 0
for i in range(1, len(hamiltonian_circuit)):
    u, v = hamiltonian_circuit[i-1], hamiltonian_circuit[i]
    total_cost += distance.euclidean(cities[u], cities[v])

# Output the result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)