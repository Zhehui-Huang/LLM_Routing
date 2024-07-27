import math
import networkx as nx
import numpy as np
from scipy.spatial.distance import pdist, squareform
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.tree.mst import minimum_spanning_tree
from itertools import combinations

# Coordinates of cities including the depot city
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate Euclidean distances
def distance(coord1, coord2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(coord1, coord2)))

# Construct the complete graph
G = nx.Graph()
for i, coord1 in cities.items():
    for j, coord2 in cities.items():
        if i != j:
            G.add_edge(i, j, weight=distance(coord1, coord2))

# Step 1: Compute MST T of G
T = minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree
O = [node for node, degree in T.degree() if degree % 2 != 0]

# Step 3: Find minimum weight perfect matching in the subgraph induced by odd degree vertices
G_odd = G.subgraph(O)
M = max_weight_matching(G_odd, maxcardinality=True, weight='weight')

# Step 4: Add the edges of M to T to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert to Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Ensure the circuit starts and ends at the depot city
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)