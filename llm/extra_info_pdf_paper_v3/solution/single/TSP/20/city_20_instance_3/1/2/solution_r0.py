import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

# Coordinates for the depot and cities
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Creating complete graph
G = nx.Graph()
n = len(coordinates)
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=euclidean_distance(coordinates[i], coordinates[j]))

# Step 1: Compute the MST
mst = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in MST
odd_degree_nodes = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

# Step 3: Minimum weight perfect matching on the odd-degree nodes
odd_graph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Add the matching edges to the MST
mst.add_edges_from(min_weight_matching)

# Step 4: Find an Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 5: Convert to Hamiltonian circuit (shortcutting)
visited = set()
hamiltonian_circuit = [0]
total_cost = 0.0

for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        total_cost += euclidean_distance(coordinates[u], coordinates[v])
        visited.add(v)

# Completing the tour by going back to the depot
hamiltonian_circuit.append(0)
total_cost += euclidean_distance(coordinates[hamiltonian_circuit[-2]], coordinates[0])

# Output the result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")