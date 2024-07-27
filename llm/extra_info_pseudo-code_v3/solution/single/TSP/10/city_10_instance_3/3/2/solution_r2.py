import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
import itertools

# Coordinates of each city, including the depot
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

# Compute a distance matrix
n = len(coords)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = np.hypot(coords[i][0] - coords[j][0], coords[i][1] - coords[j][1])

# Create the graph from the distance matrix
G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Step 1: Compute a Minimum Spanning Tree (MST) T of G
T = nx.minimum_spanning_tree(G)

# Step 2: Find the set O of vertices with odd degree
O = [x for x in T.nodes() if T.degree(x) % 2 == 1]

# Step 3: Minimum-weight perfect matching M in the induced subgraph of O
subgraph = T.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add the edges from M to T
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Eulerian circuit in H
euler_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert Eulerian to Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # returning to the depot

# Calculate the cost of the Hamiltonian circuit
total_cost = 0
for i in range(len(hamiltonian_circuit) - 1):
    total_cost += G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight']

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")