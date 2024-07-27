import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Given city coordinates
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

# Calculate distance matrix
coords = np.array(list(cities.values()))
dist_matrix = distance_matrix(coords, coords)

# Create a complete graph from distance matrix
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with odd degrees in the MST
odd_degree_nodes = [n for n in mst.nodes if mst.degree(n) % 2 == 1]

# Create subgraph for nodes with odd degree
subgraph = G.subgraph(odd_degree_nodes)
# Find the minimum weight perfect matching in the subgraph
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add the minimum weight matching edges to the MST
mst.add_edges_from(min_weight_matching)

# Construct Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(matt, source=0))  # Use the modified MST to form an Eulerian circuit

# Convert Eulerian circuit to a Hamiltonian circuit (TSP solution), removing repeated visits
visited = set()
tour = []
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)

# Ensure the tour starts and ends at the depot
tour.append(tour[0])

# Calculate the tour cost
total_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")