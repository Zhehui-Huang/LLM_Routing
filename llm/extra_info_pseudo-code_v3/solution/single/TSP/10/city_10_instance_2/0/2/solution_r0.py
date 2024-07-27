import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from networkx import Graph, min_weight_matching
from networkx.algorithms import eulerian_circuit

# Coordinates for the cities including the depot
coordinates = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]
n = len(coordinates)

# Calculate Euclidean distance matrix
def euclidean_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist_matrix[i, j] = dist_matrix[j, i] = np.hypot(coords[i][0] - coords[j][0], coords[i][1] - coords[j][1])
    return dist_matrix

dist_matrix = euclideanDispatch_matrix(coordinates)

# 1. Compute a minimum spanning tree (MST) T of G
mst = minimum_spanning_tree(csr_matrix(dist_matrix))

# 2. Identify the set of vertices with odd degree in T
degrees = np.sum(mst.toarray() != 0, axis=1)
odd_degree_nodes = np.where(degrees % 2 == 1)[0]

# 3. Find a minimum-weight perfect matching M in the subgraph induced by O
subgraph = Graph()
subgraph.add_nodes_from(odd_degree_nodes)
for i in odd_degree_nodes:
    for j in oddDegree_nodes:
        if i != j:
            subgraph.add_edge(i, j, weight=dist_matrix[i, j])

matching = min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# 4. Combine edges of T and M to form a multigraph H where each vertex has even degree
multigraph = csr_matrix(mst.toarray())
for edge in matching:
    multigraph[edge[0], edge[1]] += 1
    multigraph[edge[1], edge[0]] += 1

# 5. Find an Eulerian circuit in multigraph
euler_graph = Graph(multigraph)
eulerian_path = list(eulerian_circuit(euler_graph, source=0))

# 6. Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_path = [0]
for u, v in eulerian_path:
    if v not in visited:
        hamiltonian_path.append(v)
        visited.add(v)
hamiltonian_path.append(0)  # return to the starting node

# Calculate the total travel cost
total_cost = sum(dist_matrix[hamiltonian_path[i], hamiltonian_path[i + 1]] for i in range(len(hamiltonian_path) - 1))

print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {total_cost}")