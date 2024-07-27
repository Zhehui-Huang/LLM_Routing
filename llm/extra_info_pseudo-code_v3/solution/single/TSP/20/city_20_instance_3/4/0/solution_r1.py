import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist
from itertools import combinations

# City coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72),
}

# Create distance matrix
coords = np.array(list(cities.values()))
dist_matrix = cdist(coords, coords, metric='euclidean')

# Create the complete graph
G = nx.complete_graph(len(cities))
for i, j in combinations(cities, 2):
    G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Find a minimum spanning tree of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find odd degree vertices
odd_degree_nodes = [v for v in T.nodes() if T.degree(v) % 2 != 0]

# Step 3: Find minimum weight perfect matching
# Subgraph induced by odd degree vertices
odd_subgraph = G.subgraph(odd_degree_nodes)
# Find the minimum weight matching using networkx max_weight_matching which finds max weight matching and thus we negate the weights
min_weight_match = nx.algorithms.matching.max_weight_matching(odd_subgraph, maxcardinality=True, weight=lambda u, v, d: -d['weight'])

# Step 4: Add edges to T to form the multigraph H
H = nx.MultiGraph(T)
for u, v in min_weight_match:
    H.add_edge(u, v, weight=dist_matrix[u][v])

# Step 5: Find Eulerian circuit in multigraph H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Make Eulerian circuit Hamiltonian by removing visited nodes keeping the order
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # append the start node to make it a cycle

# Calculate the total travel cost of the tour
total_travel_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Output the result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)