import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
import itertools

# Cities coordinates
coords = {
    0: (84, 67), 
    1: (74, 40), 
    2: (71, 13), 
    3: (74, 82), 
    4: (97, 28), 
    5: (0, 31), 
    6: (8, 62), 
    7: (74, 56), 
    8: (85, 71), 
    9: (6, 76)
}

# Number of cities
num_cities = len(coords)

# Create distance matrix
distances = distance_matrix([coords[city] for city in coords], [coords[city] for city in coords])

# Create Graph
G = nx.Graph()
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=distances[i][j])

# 1. Compute MST
T = nx.minimum_spanning_tree(G)

# 2. Find vertices with odd degree
O = [v for v in T.nodes if T.degree(v) % 2 == 1]

# 3. Minimum-weight perfect matching on subgraph induced by O
subgraph = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# 4. Combine edges of T and matching to form multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# 5. Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# 6. Create Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]  # Start at the depot
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # Return to the depot

# Calculate total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")