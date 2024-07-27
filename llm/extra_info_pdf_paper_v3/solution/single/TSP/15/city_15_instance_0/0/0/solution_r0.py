import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist
from itertools import combinations

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Calculate the distance matrix
coords = np.array(list(cities.values()))
dist_matrix = cdist(coords, coords, metric='euclidean')

# Create a complete graph
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(len(cities)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find odd degree vertices in the MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Subgraph induced by odd_degree_nodes
subgraph = G.subgraph(odd_degree_nodes)

# Minimum weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add the matching edges to MST
mst.add_edges_from(matching)

# Find an Eulerian circuit in the enhanced MST
eulerian_circuit = list(nx.eulerian_circuit(mst))

# Convert the Eulerian circuit to a Hamiltonian circuit - remove repeated visits
seen = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in seen:
        hamiltonian_circuit.append(u)
        seen.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate total cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)