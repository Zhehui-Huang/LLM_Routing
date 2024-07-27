import math
from itertools import combinations
import networkx as nx
import numpy as np
from scipy.optimize import linear_sum_assignment

# Define the cities and their coordinates
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# Compute euclidean distance between cities
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Build a complete graph with weights
G = nx.Graph()
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G.add_edge(i, j, weight=euclidean_distance(coordinates[i], coordinates[j]))

# Step 1: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Compute minimum-weight perfect matching M among vertices in O
induced_subgraph = G.subgraph(O)
edge_weights = nx.get_edge_attributes(induced_subgraph, 'weight')
odd_graph = nx.complete_graph(O)
for u, v in odd_graph.edges():
    odd_graph[u][v]['weight'] = induced_subgraph[u][v]['weight'] if (u, v) in edge_weights or (v, u) in edge_weights else float('inf')

# Minimum-weight perfect matching
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.algorithms.euler.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # back to the depot

# Calculate the total travel cost of the Hamiltonian circuit
total_travel_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)