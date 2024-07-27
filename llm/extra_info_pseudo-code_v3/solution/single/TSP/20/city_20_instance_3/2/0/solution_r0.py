import networkx as nx
import numpy as np
import itertools

# Cities coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Create complete graph
G = nx.complete_graph(len(cities))
for (u, v) in G.edges():
    G[u][v]['weight'] = euclidean_distance(cities[u], cities[v])

# Step 1: Minimum Spanning Tree
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find odd degree vertices
O = [v for v in T if T.degree(v) % 2 != 0]

# Step 3: Minimum-weight perfect matching
# Create a subgraph with odd degree vertices
subgraph = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of T and M
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert to Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Ensure the tour starts and ends at the depot
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate total travel cost
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)