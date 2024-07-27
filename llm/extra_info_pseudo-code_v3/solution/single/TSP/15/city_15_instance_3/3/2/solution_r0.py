import math
from scipy.spatial.distance import pdist, squareform
import networkx as nx
import numpy as np
from itertools import combinations

# Define the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Compute Euclidean distances between each pair of cities
coords = np.array(list(cities.values()))
dist_matrix = squareform(pdist(coords, 'euclidean'))
num_cities = len(cities)

# Create a complete graph
G = nx.complete_graph(num_cities)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching in the subgraph induced by O
O_subgraph = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(O_subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and min_weight_matching to form a multigraph
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
total_cost = 0
last_visited = 0

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        total_cost += dist_matrix[last_visited][v]
        visited.add(v)
        last_visited = v

if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)
    total_cost += dist_matrix[last_visited][0]

# Output format: Tour and Total travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)