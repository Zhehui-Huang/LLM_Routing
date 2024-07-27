import math
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx
import numpy as np

# Define city coordinates
cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
          (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
          (13, 43), (61, 28), (60, 63), (93, 15)]

# Calculate distance matrix
dist_matrix = np.array([[math.hypot(cities[i][0] - cities[j][0], cities[i][1] - cities[j][1]) for j in range(len(cities))] for i in range(len(cities))])

# Compute the Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(dist_matrix)

# Graph creation from MST
G = nx.Graph(mst_matrix)

# Find nodes with an odd degree in MST
odd_degree_nodes = [node for node in G.nodes() if G.degree(node) % 2 == 1]

# Full graph to find the minimum weight perfect matching (Subgraph induced by odd degree nodes)
complete_graph = nx.Graph()
for i in odd_degree_nodes:
    for j in odd_exists if j > i:
        complete_graph.add_edge(i, j, weight=dist_matrix[i][j])

# Find minimum weight perfect matching on subgraph of nodes with odd degree
matching = nx.algorithms.matching.min_weight_matching(complete_graph, maxcardinality=True)

# Add these edges to original MST to make it Eulerian
G.add_edges_from(matching)

# Compute Eulerian circuit in the Eulerian graph
eulerian_circuit = list(nx.eulerian_circuit(G, source=0))

# Convert Eulerian circuit to Hamiltonian path
path = []
visited = set()
for u, _ in eulerian_circuit:
    if u not in visited:
        path.append(u)
        visited.add(u)

# Returning to the starting point (the depot)
path.append(path[0])

# Calculate the path cost
total_cost = sum(dist_matrix[path[i], path[i+1]] for i in range(len(path)-1))

print(f"Tour: {path}")
print(f"Total travel cost: {total_cost:.2f}")