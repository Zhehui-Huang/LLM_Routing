import math
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order
from scipy.spatial.distance import pdist, squareform
import networkx as nx

# Define city coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59),
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

# Compute distance matrix
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Convert to a sparse matrix and compute the Minimum Spanning Tree (MST)
sparse_matrix = csr_matrix(distance_matrix)
mst = minimum_spanning_tree(sparse_matrix)

# Find vertices with odd degree in the MST
mst_degrees = sum(mst.toarray() != 0, axis=0)
odd_degree_vertices = [i for i, degree in enumerate(mst_degrees) if degree % 2 == 1]

# Create a complete graph between the odd-degree vertices with distances as weights
subgraph = csr_matrix([distance_matrix[i][j] for i in odd_degree_vertices for j in odd_degree_vertices if i != j])

# Find the minimum cost perfect matching in the subgraph
G = nx.Graph()
G.add_nodes_from(odd_degree_vertices)
for i in range(len(odd_degree_vertices)):
    for j in range(i + 1, len(odd_degree_vertices)):
        G.add_edge(oddly_degree_vertices[i], odd_degree_vertices[j], weight=distance_matrix[odd_degree_vertices[i]][odd_degree_vertices[j]])

matching = nx.algorithms.matching.min_weight_matching(G, maxcardinality=True)

# Combine the edges from MST and matching to create an Eulerian circuit
graph = nx.Graph()
graph.add_edges_from(mst.toarray().nonzero())
graph.add_edges_from(matching)

# Convert the Eulerian circuit into a Hamiltonian circuit
eulerian_tour = list(nx.eulerian_circuit(graph, source=0))
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_tour:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

hamiltonian_circuit.append(0)  # Returning to the depot

# Calculate the total travel cost
total_cost = sum(distance_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)