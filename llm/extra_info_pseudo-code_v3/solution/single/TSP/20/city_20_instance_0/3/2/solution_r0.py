import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.tree.mst import minimum_spanning_tree
from networkx.algorithms.euler import eulerian_circuit

# City coordinates
coordinates = np.array([
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
])

# Calculate pairwise Euclidean distances
dist_matrix = squareform(pdist(coordinates))

# Creating a complete graph
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute a minimum spanning tree (MST)
T = minimum_spanning_tree(G, weight='weight')

# Step 2: Identify odd degree vertices
odd_degree_vertices = [v for v, degree in T.degree() if degree % 2 == 1]

# Step 3: Create minimum weight perfect matching for odd degree vertices
odd_vertex_subgraph = G.subgraph(odd_degree_vertices)
min_weight_matching = max_weight_matching(odd_vertex_subgraph, maxcardinality=True, weight='weight')

# Step 4: Add the edges in the minimum weight matching to the MST
T.add_edges_from(min_weight_matching)

# Step 5: Find Eulerian circuit
euler_circuit = list(eulerian_circuit(T, source=0))

# Step 6: Convert Eulerian to Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)

# Calculating the total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the tour and the total travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)