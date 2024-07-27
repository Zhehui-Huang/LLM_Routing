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

# Setup the complete graph with edges weighted by Euclidean distance
positions = np.array(list(cities.values()))
dist_mtx = distance_matrix(positions, positions)
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=dist_mtx[i][j])

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with an odd degree in the MST
odd_degree_nodes = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

# Subgraph induced by odd degree vertices
odd_degree_subgraph = G.subgraph(odd_degree_nodes)

# Minimum weight perfect matching on the subgraph
matching = nx.algorithms.matching.min_weight_matching(odd_degree_subgraph, maxcardinality=True, weight='weight')

# Merge MST and matching to make it Eulerian
mst.add_edges_from(matching)

# Find an Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Remove repeated visits to the same node to create the Hamiltonian circuit
tour = [0]
visited = set([0])
total_cost = 0
for u, v in eulerian_circuit:
    if v not in visited:
        tour.append(v)
        visited.add(v)
        total_cost += G[u][v]['weight']

# Return to the start point
tour.append(0)
total_cost += G[tour[-2]][0]['weight']

# Format the tour and cost output
output_tour = f"Tour: {tour}"
output_cost = f"Total travel cost: {total_cost:.2f}"

# Printing the results
print(output_tour)
print(output_cost)