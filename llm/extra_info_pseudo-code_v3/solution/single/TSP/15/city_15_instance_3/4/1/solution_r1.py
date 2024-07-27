import math
import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix
from networkx.algorithms.euler import eulerian_circuit

# Define city coordinates and their indices
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69), 
    (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate distance matrix
city_coords = np.array(cities)
dist_matrix = distance_matrix(city_coords, city_coords)

# Create graph G
G = nx.Graph()
n = len(cities)
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Step 1: Compute minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G)

# Step 2: Identify vertices with odd degree in T
O = [v for v in T.nodes if T.degree[v] % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
min_weight_matching = nx.algorithms.matching.min_weight_matching(nx.subgraph(G, O), maxcardinality=True)

# Step 4: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
euler_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # append the start city to form a complete tour

# Calculate the total travel cost of the tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltoniyour proposal. every point on the grid is assigned  a unique ID
n_circuit[1:]))

# Output the solution
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")