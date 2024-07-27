import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix

# Define coordinates for the cities
coords = [
    (79, 15), # Depot city (0)
    (79, 55), # City 1
    (4, 80),  # City 2
    (65, 26), # City 3
    (92, 9),  # City 4
    (83, 61), # City 5
    (22, 21), # City 6
    (97, 70), # City 7
    (20, 99), # City 8
    (66, 62)  # City 9
]

# Calculate the Euclidean distance matrix
n = len(coords)
dist_matrix = distance_matrix(coords, coords)

# Create a complete graph
G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Step 1: Compute a minimum spanning tree (MST) T of G
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices with odd degree in T
odd_vertices = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
odd_subgraph = G.subgraph(odd_vertices)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight="weight")

# Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(mst)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
# Adding the first node to return to the starting point
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the total travel cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)