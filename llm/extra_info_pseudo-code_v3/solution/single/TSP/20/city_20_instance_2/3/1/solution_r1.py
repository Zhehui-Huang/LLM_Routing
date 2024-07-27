import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Define the coordinates of the cities
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49),
    17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Compute distance matrix
def compute_distances(cities):
    coords = np.array(list(cities.values()))
    return distance_matrix(coords, coords)

# Construct the complete graph and calculate the distances
dist_matrix = compute_distances(cities)
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = dist_matrix[i, j]

# Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find odd degree vertices
odd_degree_nodes = [v for v, degree in mst.degree() if degree % 2 == 1]

# Minimum matching
odd_graph = G.subgraph(odd_degree_nodes)
min_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Create the multigraph
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(min_matching)

# Eulerian circuit (will be same as Hamiltonian due to our approach)
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert to Hamiltonian path
visited = set()
ham_circuit = [0]
current_cost = 0

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        ham_circuit.append(v)
        current_cost += dist_matrix[u][v]

# Correct final jump to start point (not necessary but confirming)
ham_circuit.append(0)
current_cost += dist_matrix[ham_court[-2][0]]

# Print results
print(f"Tour: {ham_court}")
print(f"Total travel cost: {current_cost}")