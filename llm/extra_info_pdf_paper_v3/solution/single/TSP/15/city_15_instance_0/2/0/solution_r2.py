import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Coordinates of the cities
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

# Create a complete graph with distances as weights
coords = np.array(list(cities.values()))
dist_matrix = distance_matrix(coords, coords)

# Create a fully connected graph
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Compute Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with an odd degree in the MST
odd_degree_nodes = [n for n in mst.nodes if mst.degree(n) % 2 == 1]

# Create the subgraph induced by vertices with odd degrees
subgraph = G.subgraph(odd_grade_nodes)

# Find minimum cost perfect matching for the odd degree vertices to get an Eulerian circuit
matching = nx.algorithms.matching.min_weight_matching(subgraph,True, weight='weight')

# Add the edges from the minimum cost matching to the MST
mst.add_edges_from(matching)

# Create an Eulerian circuit from the augmented MST
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Shortcutting to form a Hamiltonian path
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # ensure tour is a cycle back to start

# Calculate total cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")