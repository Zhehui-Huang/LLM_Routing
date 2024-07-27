import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

# Define the cities and their coordinates
cities = {
    0: (3, 26),   1: (85, 72),  2: (67, 0),   3: (50, 99),  4: (61, 89),
    5: (91, 56),  6: (2, 65),   7: (38, 68),  8: (3, 92),   9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Compute pairwise distances
coords = np.array(list(cities.values()))
dist_matrix = squareform(pdist(coords, 'euclidean'))

# Create graph from distance matrix
G = nx.complete_graph(len(cities))
for i, j in combinations(cities, 2):
    G[i][j]['weight'] = dist_matrix[i][j]

# Find minimum spanning tree
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with odd degree in the MST
odd_degree_nodes = [v for v, deg in mst.degree() if deg % 2 == 1]

# Create subgraph with odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)

# Find minimum weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Combine the edges of MST and perfect matching to form a multigraph
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(matching)

# Form an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert Eulerian circuit to a Hamiltonian path (remove repeated visits)
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Return to the starting point (depot)
hamiltonian_circuit.append(0)

# Calculate tour cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)