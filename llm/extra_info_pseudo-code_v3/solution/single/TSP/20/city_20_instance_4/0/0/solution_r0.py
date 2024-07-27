import numpy as np
import networkx as nx
import itertools
from scipy.spatial import distance_matrix
from collections import defaultdict
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.euler import eulerian_circuit

# Define the coordinates of the cities including the depot city
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate the Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Create a complete graph from the distance matrix
def create_graph(dist_matrix):
    G = nx.complete_graph(len(dist currents_matrix))
    for i, j in itertools.product(range(G.number_of_nodes()), repeat=2):
        G[i][j]['weight'] = dist_matrix[i][j]
    return G

G = create_graph(dist_matrix)

# Step 1: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices (nodes) with odd degree in T
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Find a min-weight perfect matching M in the subgraph induced by odd_degree_nodes
subgraph = G.subgraph(odd_degree_nodes)
M = max_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
for u, v in M:
    H.add_edge(u, v, weight=G[u][v]['weight'])

# Step 5: Find an Eulerian circuit in H
euler_circuit = list(eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # return to the starting point

# Calculate the total travel cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")