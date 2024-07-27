import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx
from networkx.algorithms.matching import max_weight_matching

# List of city coordinates
coordinates = [
    (50, 42), # Depot city 0
    (41, 1),  # City 1
    (18, 46), # City 2
    (40, 98), # City 3
    (51, 69), # City 4
    (47, 39), # City 5
    (62, 26), # City 6
    (79, 31), # City 7
    (61, 90), # City 8
    (42, 49)  # City 9
]

# Creating distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Construct complete graph
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        G.edges[i, j]['weight'] = dist_matrix[i][j]

# Step 1: Compute a minimum spanning tree T of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree in T
odd_degree_nodes = [v for v, degree in dict(T.degree()).items() if degree % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O using max_weight_matching
subgraph = G.subgraph(odd_degree_nodes)
M = max_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
euler_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit (shortcutting visited nodes)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # Closing the tour at the start point

# Calculate the total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Print results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")