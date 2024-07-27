import networkx as nx
import numpy as np
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

# Step 1: Compute a minimum spanning tree (MST) T of G.
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices with odd degree in T.
O = [v for v in T if T.degree(v) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O.
subgraph = G.subgraph(O)
M = nx.Graph()
min_weight_match = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
M = G.edge_subgraph(min_weight_match).copy()

# Step 4: Combine the edges of T and M to form a multigraph H where each vertex has even degree.
H = nx.MultiGraph()
H.add_edges_from(T.edges())
H.add_edges_from(M.edges())

# Step 5: Find an Eulerian circuit in H.
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices.
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)

# Add start vertex to complete the cycle
hamiltonian_circuit.append(0)

# Calculate the total travel cost of the tour
total_cost = 0
for i in range(len(hamiltonian_circuit) - 1):
    u, v = hamiltonian_circuit[i], hamiltonian_circuit[i+1]
    total_cost += G[u][v]['weight']

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")