import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from networkx import Graph, eulerian_circuit, minimum_weight_full_matching

# Define cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate the distance matrix
coordinates = np.array(list(cities.values()))
dist_matrix = squareform(pdist(coordinates, metric='euclidean'))

# Convert into CSR Matrix
csr_dist_matrix = csr_matrix(dist_matrix)

# Compute Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(csr_dist_matrix)

# Find vertices in MST with odd degree
odd_degree_vertices = [node for node, degree in enumerate(mst.toarray().astype(bool).sum(axis=0) + mst.toarray().astype(bool).sum(axis=1)) if degree % 2 == 1]

# Create subgraph with odd degree vertices
odd_graph = csr_matrix(dist_matrix[np.ix_(odd_degree_vertices, odd_degree_vertices)])

# Compute Minimum Weight Perfect Matching on the subgraph
matching_graph = Graph()
matching_graph.add_nodes_from(odd_degree_vertices)
for i in range(len(odd_degree_vertices)):
    for j in range(i + 1, len(odd_degree_vertices)):
        weight = dist_matrix[odd_degree_vertices[i], odd_degree_vertices[j]]
        matching_graph.add_edge(odd_degree_vertices[i], odd_degree_vertices[j], weight=weight)

matching = minimum_weight_full_matching(matching_graph, weight='weight')

# Combine the edges of MST and matching to get the Eulerian Multigraph
multi_graph = np.array(mst.toarray())
for u, v in matching.items():
    multi_graph[u, v] += 1
    multi_graph[v, u] += 1

# Compute Eulerian circuit
euler_graph = Graph(multi_graph)
circuit = list(eulerian_circuit(euler_graph, source=0))

# Convert circuit to Hamiltonian circuit by visiting each city only once
hamiltonian_circuit = [0]
visited = set([0])
for u, v in circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Close the circuit back to the starting point
hamiltonian_circuit.append(0)

# Calculate the total cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)