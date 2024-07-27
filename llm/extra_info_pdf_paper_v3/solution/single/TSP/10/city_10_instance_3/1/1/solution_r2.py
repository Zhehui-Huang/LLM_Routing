import numpy as np
import networkx as nx
from math import sqrt

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76),
}

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Generate graph from distance matrix
G = nx.from_numpy_matrix(distance_matrix)

# Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find odd degree vertices in MST
odd_degree_nodes = [n for n, d in mst.degree() if d % 2 == 1]

# Form complete graph on odd degree nodes
odd_graph = nx.complete_graph(odd_degree_nodes)

# Update graph weights
for (u, v) in odd_graph.edges():
    odd_graph[u][v]['weight'] = distance_matrix[u][v]

# Find minimum weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add matching edges to the MST
mst.add_edges_from(matching)

# Create an eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert eulerian circuit to a simple path
tour = []
visited = set()

for u, v in eulerian_n:
    if u not in visited:
        tour.append(u)
        visited.add(u)
tour.append(0)  # Return to the starting node, if not already included

# Calculate the total travel cost
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")