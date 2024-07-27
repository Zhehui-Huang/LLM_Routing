import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist
from itertools import combinations

# Define city coordinates
coordinates = np.array([
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
])

# Compute the Euclidean distance matrix
distance_matrix = cdist(coordinates, coordinates, metric='euclidean')

# Create a complete graph from the distance matrix
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G[i][j]['weight'] = distance_matrix[i][j]

# 1. Compute a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# 2. Find vertices with an odd degree
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# 3. Create the subgraph induced by nodes with odd degree
odd_subgraph = G.subgraph(odd_degree_nodes)
odd_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# 4. Combine edges of MST and Minimum Weight Perfect Matching
mst.add_edges_from(odd_matching)

# 5. Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# 6. Convert to a Hamiltonian circuit by skipping repeated nodes
# Maintain a set of visited nodes to avoid repetitions and form the tour
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # Ensure to return to the starting point

# Calculate the tour cost
tour_cost = sum(distance_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the tour and the total cost
print("Tour:", hamiltonian_circuit)
print(f"Total travel cost: {tour_cost:.2f}")