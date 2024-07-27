import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

# Given coordinates of the cities including the depot
coordinates = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Function to compute Euclidean distance matrix
def calculate_distance_matrix(coords):
    return squareform(pdist(coords, 'euclidean'))

# Distance matrix
dist_matrix = calculate_distance_matrix(coordinates)

# Create a complete graph from distance matrix
def create_complete_graph(dist_matrix):
    G = nx.Graph()
    for i, j in combinations(range(len(distArray)), 2):
        G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

G = create_complete_graph(dist_matrix)

# 1. Compute the Minimum Spanning Tree (MST)
mst_tree = nx.minimum_spanning_tree(G, weight="weight")

# 2. Find vertices with odd degree
odd_degree_vertices = [v for v, d in mst_tree.degree() if d % 2 == 1]

# 3. Find minimum weight perfect matching on the subgraph induced by vertices with odd degree
odd_graph = G.subgraph(odd_degree_vertices)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight="weight")

# 4. Add matching edges to MST
mst_tree.add_edges_from(min_weight_matching)

# 5. Find Eulerian circuit
eulerian_path = list(nx.eulerian_circuit(mst_tree, source=0))

# 6. Create a Hamiltonian circuit (avoid repeated nodes)
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_path:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Calculate the total travel cost
total_travel_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_travel_analysis:.2f}")