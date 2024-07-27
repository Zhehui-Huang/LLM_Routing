import numpy as np
from scipy.spatial.distance import pdist, squareform
import networkx as nx
import itertools

# City coordinates
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), (61, 16),
    (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

# Compute the Euclidean distance matrix
distance_matrix = squareform(pdist(coordinates, metric='euclidean'))

# Build a Graph with distances as edge weights
G = nx.Graph()
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G.add_edge(i, j, weight=distance_matrix[i][j])

# Step 1: Compute Minimum Spanning Tree (MST)
min_span_tree = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in MST
odd_degree_vertices = [v for v, degree in min_span_tree.degree() if degree % 2 == 1]

# Step 3: Minimum Weight Perfect Matching on subgraph of odd degree vertices
odd_vertex_subgraph = G.subgraph(odd_fee_vertices)
matching = nx.algorithms.matching.min_weight_matching(odd_vertex_subgraph, maxcardinality=True, weight='weight')

# Add the matching edges to the MST to get a multigraph
min_span_tree.add_edges_from(matching)

# Step 4: Find an Eulerian tour in the multigraph
euler_tour = list(nx.eulerian_circuit(min_span_tree, source=0))

# Step 5: Convert Eulerian tour to Hamiltonian path by skipping repeated vertices
visited = set()
hamiltonian_path = []
for u, v in euler_tour:
    if u not in visited:
        hamiltonian_path.append(u)
        visited.add(u)
# Append the starting node to complete the circuit
hamiltonian_path.append(0)

# Calculate total cost of the tour
total_distance = sum(distance_matrix[hamiltonian_path[i]][hamiltonian_path[i+1]] for i in range(len(hamiltonian_path) - 1))

# Produce the final output
print("Tour: ", hamiltonian_path)
print("Total travel cost: ", total_distance)