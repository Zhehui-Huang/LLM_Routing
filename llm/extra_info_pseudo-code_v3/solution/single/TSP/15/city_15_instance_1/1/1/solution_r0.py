import numpy as np
import networkx as nx
from itertools import combinations
from scipy.spatial.distance import pdist, squareform
from scipy.optimize import linear_sum_assignment

# Coordinates of cities including the depot
cities_coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Number of cities
n = len(cities_coordinates)

# Compute pairwise Euclidean distance matrix
dist_matrix = squareform(pdist(cities_coordinates))

# Create complete graph from distance matrix
G = nx.complete_graph(n)
for i, j in combinations(range(n), 2):
    G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices of odd degree
odd_degree_nodes = [node for node in mst.nodes if mst.degree[node] % 2 == 1]

# Step 3: Minimum-weight perfect matching
odd_graph = G.subgraph(odd_degree_nodes)
odd_graph_weights = nx.get_edge_attributes(odd_graph, 'weight')
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, weight='weight', maxcardinality=True)

# Step 4: Add edges of the matching to the MST
mst.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit (shortcutting)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # to return to the depot

# Calculate total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)