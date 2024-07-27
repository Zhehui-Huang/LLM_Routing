import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import itertools

# Define the positions of cities
positions = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57),
    6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Create a complete graph
G = nx.complete_graph(len(positions))

# Add distances as edge weights
for u, v in G.edges():
    pos_u, pos_v = positions[u], positions[v]
    distance = np.sqrt((pos_u[0] - pos_v[0])**2 + (pos_u[1] - pos_v[1])**2)
    G[u][v]['weight'] = distance

# Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Identify vertices with odd degree from T
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Create the induced subgraph on vertices with odd degree
subgraph = G.subgraph(O)

# Find the minimum weight perfect matching in the induced subgraph
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Forming a multigraph H by combining T and the matching edges
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Create an Eulerian circuit from H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Convert the Eulerian circuit to a Hamiltonian path (TSP path)
visited = set()
hamiltonian_path = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_path.append(u)
        visited.add(u)

# Add the starting node to complete the cycle
hamiltonian_path.append(0)

# Calculate the total length of the path
total_length = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_path[:-1], hamiltonian_path[1:]))

# Display the results
print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {total_length}")