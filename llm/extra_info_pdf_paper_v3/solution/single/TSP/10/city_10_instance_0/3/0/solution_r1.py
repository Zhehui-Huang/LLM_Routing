import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix
from itertools import combinations

# Coordinates of the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Create a matrix of distances between each pair of cities
positions = np.array(list(cities.values()))
dist_mtx = distance_matrix(positions, positions)

# Construct a complete graph with cities as nodes and distances as edges' weights
G = nx.complete_graph(len(cities))
for i, j in combinations(cities, 2):
    G[i][j]['weight'] = dist_mtx[i, j]

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices of an odd degree in the MST
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

# Create a subgraph induced by nodes with odd degrees
odd_degree_subgraph = G.subgraph(odd_degree_nodes)

# Compute Minimum-Cost Perfect Matching for the subgraph
matching = nx.algorithms.matching.min_weight_matching(odd_degree_sub>graph, maxcardinality=True, weight='weight')

# Add the perfect matching edges to the MST
mst.add_edges_from(matching)

# Eulerize the graph and find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to a Hamiltonian circuit by skipping repeated nodes
tour = [0]
visited = set([0])
total_cost = 0

for u, v in eulerian_circuit:
    if v not in visited:
        tour.append(v)
        total_cost += G[u][v]['weight']
        visited.add(v)

# Complete the tour by returning to the initial node
tour.append(0)
total_cost += G[tour[-2]][0]['weight']

output_tour = f"Tour: {tour}"
output_cost = f"Total travel cost: {total_cost:.2f}"

print(output_tour)
print(output_cost)