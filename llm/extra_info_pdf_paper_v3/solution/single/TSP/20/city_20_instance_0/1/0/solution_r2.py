import math
import networkx as nx
from itertools import combinations

# Define city coordinates
cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
          (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
          (13, 43), (61, 28), (60, 63), (93, 15)]

# Calculate distance matrix
dist_matrix = [[math.hypot(cities[i][0] - cities[j][0], cities[i][1] - cities[j][1]) for j in range(len(cities))] for i in range(len(cities))]

# Create a complete graph
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find nodes with an odd degree
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

# Create a complete graph on the odd degree nodes
odd_graph = nx.Graph()
for u, v in combinations(odd_degree_nodes, 2):
    odd_graph.add_edge(u, v, weight=dist_matrix[u][v])

# Find minimum weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(odd_graph, True)

# Add edges from the matching to the MST
mst.add_edges_from(matching)

# Find an Eulerian tour on the graph
eulerian_tour = nx.eulerian_circuit(mst, source=0)

# Convert Eulerian tour to a Hamiltonian path by skipping visited nodes
visited = set()
tour = []
for (u, _) in eulerian_tour:
    if u not in visited:
        tour.append(u)
        visited.add(u)
tour.append(0)  # Return to the starting node

# Calculate the cost of the tour
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Return the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")