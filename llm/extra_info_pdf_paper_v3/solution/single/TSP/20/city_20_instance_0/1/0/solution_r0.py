import math
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from networkx import from_numpy_matrix, relabel_nodes, Graph, eulerian_circuit
import networkx.algorithms.matching as max_weight_matching
import numpy as np

# Define city coordinates
cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
          (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
          (13, 43), (61, 28), (60, 63), (93, 15)]

# Calculate distance matrix
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

dist_matrix = np.array([[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))])

# Compute the Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(dist_matrix).toarray()

# Create graph from MST
G = from_numpy_matrix(mst_matrix)

# Find nodes with an odd degree
odd_degree_nodes = [v for v in G.nodes() if G.degree(v) % 2 != 0]

# Get the subgraph induced by nodes with odd degree
odd_graph = G.subgraph(odd_degree_nodes)

# Calculate the minimum weight matching for the nodes with odd degree
odd_matching = max_weight_matching.max_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add edges from matching to the MST
for edge in odd_matching:
    G.add_edge(edge[0], edge[1])

# Compute Eulerian circuit
ec = list(eulerian_circuit(G, source=0))

# Convert Eulerian circuit to path by skipping revisited nodes
visited = set()
tour = []
for u, v in ec:
    if u not in visited:
        tour.append(u)
        visited.add(u)
    if v not in visited:
        tour.append(v)
        visited.add(v)

# Ensure the tour starts and ends at the depot (0)
tour = [0] + [node for node in tour if node != 0] + [0]

# Calculate the tour cost
total_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")