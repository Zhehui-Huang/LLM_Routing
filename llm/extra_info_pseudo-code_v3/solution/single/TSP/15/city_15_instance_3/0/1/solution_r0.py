import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Compute distance matrix
distance_matrix = np.array([[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))])

# Compute the Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(distance_matrix)

# Convert MST result into a graph
G = nx.Graph()
G.add_weighted_edges_from((i, j, distance_matrix[i][j]) for i in range(len(cities)) for j in range(len(cities)) if mst_matrix[i, j] > 0)

# Find odd degree vertices
odd_degree_nodes = [v for v, d in G.degree() if d % 2 != 0]

# Compute minimum weight perfect matching
min_weight_matching = nx.algorithms.matching.min_weight_matching(nx.subgraph(G, odd_degree_nodes), maxcardinality=True, weight='weight')

# Add matching edges to MST graph
G.add_edges_from(min_weight * 2 for min_weight in min_weight_matching)  

# Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(G, source=0))

# Convert the Eulerian circuit to a Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)

# Add the start point at the end to complete the circuit
hamiltonian_circuit.append(0)

# Calculate the total cost of the Hamiltonian circuit
total_cost = sum(distance_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")