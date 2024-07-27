import networkx as nx
import numpy as,from itertools import combinations
import math

# City coordinates
coordinates = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 
    4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31), 
    8: (61, 90), 9: (42, 49)
}

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph with cities as nodes
G = nx.Graph()
for node in coordinates:
    G.add_node(node)
for (node1, node2) in combinations(coordinates, 2):
    G.add_edge(node1, node2, weight=euclidean_distance(coordinates[node1], coordinates[node2]))

# Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find nodes with odd degree
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 == 1]

# Create the minimum weight perfect matching graph for odd degree nodes
odd_graph = nx.Graph()
odd_graph.add_nodes_from(odd_degree_nodes)
for (node1, node2) in combinations(odd_degree_nodes, 2):
    odd_graph.add_edge(node1, node2, weight=euclidean_distance(coordinates[node1], coordinates[node2]))

# Calculate minimum weight perfect matching to add to the MST
matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add the matched edges to the MST
mst.add_edges_from(matching)

# Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Making it a Hamiltonian circuit: remove visited nodes, keeping first occurrence
visited = set()
tour = []
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
    if v not in visited:
        tour.append(v)
        visited.add(v)
tour.append(tour[0])  # to return to the start

# Calculate the total cost of the tour
total_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)