from scipy.spatial import distance_matrix
import numpy as np
from networkx import Graph, minimum_spanning_tree, find_odd_degree_nodes, eulerian_circuit
from networkx.algorithms.matching import min_weight_matching
import itertools

# City coordinates
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), (61, 16),
    (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

# Calculate the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Create a Graph and add the edges with weights
G = Graph()
num_cities = len(coordinates)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Step 1: Compute a Minimum Spanning Tree
T = minimum_spanning_tree(G)

# Step 2: Find odd degree vertices
O = [v for v, d in T.degree if d % 2 == 1]

# Step 3: Create subgraph induced by odd degree vertices and find minimum weight perfect matching
O_subgraph = G.subgraph(O)
M = min_weight_matching(O_subgraph, maxcardinality=True, weight='weight')

# Add matching edges to the MST
T.add_edges_from(M)

# Step 4: Form a multigraph H (done by combining T and M) and find an Eulerian circuit
E = list(eulerian_circuit(T, source=0))

# Step 5 and 6: Convert Eulerian circuit to Hamiltonian circuit (shortcut non-repeated)
visited = set()
hamiltonian_circuit = []
for u, v in E:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
        
# Ensure the tour starts and ends at the depot city 0
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate the total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")