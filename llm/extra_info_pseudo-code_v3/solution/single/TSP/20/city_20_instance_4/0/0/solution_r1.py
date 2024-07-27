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
    (82, 48), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate the Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Create a complete graph from the distance matrix
def create_graph(dist_matrix):
    G = nx.Graph()
    for i, j in itertools.product(range(len(dist_matrix)), range(len(dist_matrix))):
        if i != j:
            G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

G = create_graph(dist_matrix)

# Step 1: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices (nodes) with odd degree in T
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Find a min-weight perfect matching M in the subgraph induced by odd_degree_nodes
subgraph = G.subgraph(odd_degree_nodes)
M = max_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Adding the matched edges to the tree
H = T.copy()
for edge in M:
    H.add_edge(edge[0], edge[1], weight=G[edge[0]][edge[1]]['weight'])

# Step 5: Find an Eulerian circuit in H
circuit = list(eulerian_circuit(H, source=0))

# Step 6: Create a Hamiltonian circuit by removing repeated vertices, keeping the first occurrence
visited = set()
hamiltonian_circuit = []
for u, v in circuit:
    if not u in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # to make a complete tour returning to the depot

# Calculate the total travel cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")