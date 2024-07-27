import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.euler import eulerian_circuit

# Define the coordinates of cities including the depot
coords = np.array([
    (9, 93),   # Depot - city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
])

# Calculate the distance matrix using Euclidean distance
dist_matrix = distance_matrix(coords, coords)

# Create a graph with cities as nodes
G = nx.complete_graph(len(coords))
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Identify nodes of odd degree in MST
odd_degree_nodes = [node for node, degree in mst.degree() if degree % 2 == 1]

# Subgraph induced by nodes of odd degree
subgraph = G.subgraph(odd_degree_nodes)

# Get minimum weight perfect matching on the subgraph
matching = max_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add these edges to the MST
mst.add_edges_from(matching)

# Form Eulerian circuit from the resultant graph
euler_tour = list(eulerian_circuit(mst, source=0))

# Remove repeated nodes except for initial vertex to form a Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
for u, v in euler_tour:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Calculate the total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(-1, len(hamiltonian_circuit) - 1))

# Output the final tour and the travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)