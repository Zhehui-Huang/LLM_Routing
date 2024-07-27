import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Calculate the distance matrix
coords = np.array(list(cities.values()))
dist_matrix = cdist(coords, coords, metric='euclidean')

# Create a complete graph
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(len(cities)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find odd degree vertices in the MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Create a subgraph G' from G that covers all odd-degree vertices in MST
subgraph = G.subgraph(odd_degree_nodes)

# Compute minimum weight perfect matching to make all nodes deg even in the subgraph
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add the matched edges to MST to make it an Eulerian circuit
mst.add_edges_from(matching)

# Find an Eulerian circuit in the Eulerian enhanced MST
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert the Eulerian circuit to a Hamiltonian circuit by removing repeated nodes
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)

# Adding the start node to complete the circuit
hamiltonian_circuit.append(0)

# Calculate total cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Print results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)