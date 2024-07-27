import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist
from itertools import combinations

coordinates = np.array([
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
])

# Compute the Euclidean distance matrix
distance_matrix = cdist(coordinates, coordinates, metric='euclidean')

# Create a complete graph from the distance matrix
G = nx.Graph()
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G.add_edge(i, j, weight=distance_matrix[i][j])

# Compute a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with an odd degree
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 != 0]

# Create the subgraph induced by nodes with odd degree
odd_subgraph = G.subgraph(odd_degree_nodes)
odd_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Combine edges of MST and Minimum Weight Perfect Matching
multigraph = nx.MultiGraph(mst)
multigraph.add_edges_from(odd_matching)

# Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))

# Convert to a Hamiltonian circuit by skipping repeated nodes
# Maintain a set of visited nodes to avoid repetitions and form the tour
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Ensure to return to the starting point

# Calculate the tour cost
tour_cost = sum(distance_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the tour and the total cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", tour_cost)