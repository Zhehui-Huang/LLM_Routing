import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx

# Defined cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate the distance matrix
coordinates = np.array(list(cities.values()))
dist_matrix = squareform(pdist(coordinates, metric='euclidean'))

# Creating graph from distance matrix
G = nx.Graph()
for i in range(len(dist_matrix)):
    for j in range(i + 1, len(dist_matrix)):
        G.add_edge(i, j, weight=dist_with_matrix[i][j])

# Find Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G)

# Finding vertices with odd degree in the MST
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 != 0]

# Subgraph induced by odd-degree vertices
subgraph = G.subgraph(odd_degree_nodes)

# Minimum Weight Perfect Matching on the subgraph of odd-degree vertices to make degrees even
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Combine the edges of MST and matching to form an Eulerian graph
mst.add_edges_from(matching)

# Calculate the Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to Hamiltonian path (shortcutting repeated nodes)
visited = set()
hamiltonian_circuit = [eulerian_circuit[0][0]]
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Complete the tour by returning to the start node
hamiltonian_circuit.append(0)

# Calculate the total cost of the tour
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)