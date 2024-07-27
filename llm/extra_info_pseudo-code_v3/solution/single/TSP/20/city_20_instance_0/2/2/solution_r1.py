import networkx as nx
import numpy as np
from itertools import combinations

# Cities coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Distance function
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create complete graph
G = nx.complete_graph(len(cities))
for u, v in G.edges():
    G[u][v]['weight'] = distance(u, v)

# Minimum Spanning Tree (MST) of G
T = nx.minimum_spanning_tree(G)

# Find vertices with odd degree in T
O = [v for v in T if T.degree(v) % 2 == 1]

# Complete graph on vertices in O
M = nx.Graph()
M.add_nodes_from(O)
for u, v in combinations(O, 2):
    M.add_edge(u, v, weight=distance(u, v))

# Minimum weight perfect matching in the subgraph induced by O
min_matching = nx.algorithms.matching.min_weight_matching(M, maxcardinality=True, weight='weight')

# Add the edges from the minimum perfect matching to the tree
H = nx.MultiGraph(T)
H.add_edges_from(min_matching)

# Compute the Eulerian circuit on multi-graph H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Convert the Eulerian circuit to Hamiltonian path
visited = set()
hamiltonian_circuit = []

for v in eulerian_circuit:
    if v[0] not in visited:
        hamiltonian_circuit.append(v[0])
        visited.add(v[0])

# Ensure returning to the start point
hamiltonian_circuit.append(hamiltonian_circuit[0])  # complete the circuit by returning to the initial node

# Calculate total distance of the Hamiltonian circuit
total_distance = sum(distance(hamiltonian_circuit[i], hamiltonian_circuit[i+1]) for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_distance)