import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

# Define city coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Create a complete graph
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute a minimum spanning tree T
T = nx.minimum_spanning_tree(G)

# Step 2: Identify vertices with odd degree in T
vertices_odd_degree = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Minimum-weight perfect matching M on the subgraph induced by vertices with odd degree
# Extract the subgraph
subgraph = G.subgraph(vertices_odd_view)
odd_vertex_pairs = list(itertools.combinations(subgraph.nodes(), 2))
# Create a complete graph from the odd degree vertices
odd_graph = nx.Graph()
for (u, v) in odd_vertex_pairs:
    odd_graph.add_edge(u, v, weight=dist_matrix[u][v])

# Find the minimum weight perfect matching
mate = nx.algorithms.matching.min_weight_matching(odd_graph, True)

# Step 4: Combine edges of T and M
multigraph = nx.MultiGraph(T)
multigraph.add_edges_from(mate)

# Step 5: Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))

# Step 6: Convert to Hamiltonian circuit, skipping repeated vertices
visited = set()
hamiltonian_circuit = [0]
for u, v in euleranimate_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
hamiltonian_circuit.append(0)  # Returning to the starting node

# Calculating the total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)