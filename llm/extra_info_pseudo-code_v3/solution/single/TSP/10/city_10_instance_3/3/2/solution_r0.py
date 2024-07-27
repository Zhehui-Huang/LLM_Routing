import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

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

# Create distance matrix
cities = list(coords.keys())
distances = distance_matrix([coords[city] for city in cities], [coords[city] for city in cities])

# Create Graph
G = nx.Graph()
for i, j in combinations(cities, 2):
    G.add_edge(i, j, weight=distances[i][j])

# 1. Compute MST
T = nx.minimum_spanning_tree(G)

# 2. Find vertices with odd degree
O = [v for v in T.nodes() if T.degree[v] % 2 == 1]

# 3. Minimum-weight perfect matching on subgraph induced by O
subgraph = G.subgraph(O)
min_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# 4. Add matching edges to MST
H = nx.Graph(T)
H.add_edges_from(min.binding)

# 5. Find Eulerian circuit
euler_circuit = list(nx.eulerian_circuit(H))

# 6. Make Hamiltonian by skipping visited vertices
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if not visited:
        hamiltonian_circuit.append(u)
    visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
    visited.add(v)
# Ensure it ends at the depot and is a cycle
if hamiltonian_circuit[0] != 0:
    hamiltonian_circuit.append(0)

# Calculate total travel cost
total_cost = sum(G.edges[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]]['weight']
                 for i in range(len(hamiltolian_circuit)-1))

# Output the result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")