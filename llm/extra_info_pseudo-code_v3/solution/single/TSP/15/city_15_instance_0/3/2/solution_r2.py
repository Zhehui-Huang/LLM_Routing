import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

# City coordinates
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Step 1: Compute the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Creating a complete graph from the distance matrix
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 2: Compute a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 3: Find vertices with odd degrees in MST
odd_vertices = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

# Step 4: Find minimum-weight perfect matching among the odd degree vertices
odd_graph = G.subgraph(odd_vertices)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Combine the edges of MST and Matching to form a multigraph
mst.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Convert Eulerian circuit into a Hamiltonian circuit skipping repeated vertices
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # Ensure it returns to the starting node, the depot.

# Compute the total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)