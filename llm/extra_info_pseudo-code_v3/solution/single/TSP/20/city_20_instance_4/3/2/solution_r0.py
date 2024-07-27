import networkx as nx
import numpy as np
from itertools import combinations
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from networkx.algorithms.matching import min_weight_matching
from networkx.algorithms.euler import eulerian_circuit

# Coordinates of each city, city index is the position in the list
coords = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Compute the pairwise Euclidean distance matrix
dist_matrix = squareform(pdist(coords, metric='euclidean'))

# Create a complete graph with 20 nodes
G = nx.complete_graph(len(coords), create_using=nx.Graph)

# Set weights for each edge in graph based on distances
for i, j in combinations(range(len(coords)), 2):
    G.edges[i, j]['weight'] = dist_matrix[i][j]

# Step 1: Compute Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degrees in the MST
odd_degree_nodes = [v for v, degree in dict(T.degree()).items() if degree % 2 == 1]

# Step 3: Compute Minimum Weight Perfect Matching on the induced subgraph by odd_degree_nodes
subgraph = G.subgraph(odd_degree_nodes)
min_matching = min_weight_matching(subgraph, weight='weight', maxcardinality=True)

# Step 4: Add edges from min_matching to the MST to create multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_matching)

# Step 5: Find Eulerian Circuit
euler_circuit = list(eulerian_circuit(H, source=0))

# Step 6: Make Hamiltonian circuit by skipping repeated nodes
visited = set()
hamiltonian_circuit = [0]
for u, v in euler_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Output the tour
print(f"Tour: {hamiltonian_circuit}")

# Calculate the total cost of the journey
total_cost = sum(G.edges[hamiltonian_circuit[i], hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit)-1))
print(f"Total travel cost: {total_cost}")