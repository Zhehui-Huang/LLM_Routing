import math
import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix

# Define coordinates of the cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Create the distance matrix
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a complete graph with distances as weights
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Compute MST T from Graph G
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Minimum weight perfect matching on subgraph induced by O
odd_subgraph = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Step 4: Combine T and min_weight_matching
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find Eulerian circuit in H
circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert to Hamiltonian circuit by skipping visited nodes
visited = set()
hamiltonian_circuit = []
for u, v in circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # return to the starting point

# Calculate total cost of the Hamiltonian circuit
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Print results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")