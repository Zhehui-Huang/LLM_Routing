import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Define the cities coordinates array
cities = np.array([
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
])

# Calculate the Euclidean distance matrix
dist_matrix = distance_matrix(cities, cities)

# Step 2: Create Minimum Spanning Tree (MST) using the distance matrix
mst_matrix = minimum_spanning_tree(dist_matrix)

# Step 3: Find vertices with odd degrees in MST
# Convert the MST to CSR format
mst_csr = csr_matrix(mst_matrix)
degrees = np.array(mst_csr.sum(axis=0))[0] + np.array(mst_csr.sum(axis=1).T)[0]
odd_vertices = np.where(degrees % 2 == 1)[0]

# Step 4: Minimum weight perfect matching for odd_degree vertices
def minimum_weight_perfect_matching(odd_vertices, dist_matrix):
    odd_graph = nx.Graph()
    # Subset the distance matrix into odd vertex subgraph
    submatrix = dist_matrix[np.ix_(odd_vertices, odd_vertices)]
    for i in range(len(odd_vertices)):
        for j in range(i + 1, len(odd_vertices)):
            if i != j:
                weight = submatrix[i, j]
                odd_graph.add_edge(odd_vertices[i], odd_vertices[j], weight=weight)
    # Compute the matching
    matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)
    return matching

matching = minimum_weight_perfect_matching(odd_vertices, dist_matrix)
# Adding the MST and the matching to create multigraph with even degree
graph = nx.from_scipy_sparse_matrix(mst_csr, edge_attribute='weight')
graph.add_edges_from(matching)

# Step 5: Find Eulerian circuit from graph
eulerian_circuit = nx.eulerian_circuit(graph, source=0)

# Convert circuit to Hamiltonian path (Hamiltonian circuit)
visited = set()
hamiltonian_path = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_path.append(v)
    if len(visited) == len(cities) - 1:
        break
hamiltonian_path.append(0)  # Return to start

# Calculate the total travel cost of the tour
total_cost = sum(dist_matrix[hamiltonian_path[i], hamiltonian_path[i + 1]] for i in range(len(hamiltonian_path) - 1))

print(f'Tour: {hamiltonian_path}')
print(f'Total travel cost: {total_cost}')