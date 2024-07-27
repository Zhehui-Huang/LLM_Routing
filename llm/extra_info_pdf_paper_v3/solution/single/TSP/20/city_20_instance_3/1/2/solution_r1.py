import networkx as nx
import numpy as np
from scipy.spatial import distance

# Defining the coordinates of the cities
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Number of cities including the depot
num_cities = len(coordinates)

# Calculating distance matrix
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i][j] = distance.euclidean(coordinates[i], coordinates[j])

# Create a graph from the distance matrix
G = nx.complete_graph(num_cities)
for i in range(num_cities):
    for j in range(i+1, num_cities):
        G[i][j]['weight'] = dist_matrix[i][j]

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find odd degree vertices in the MST
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 != 0]

# At this point, the minimum_weight_full_matching function is relevant to induce minimum cost perfect matching in a subgraph of odd degree nodes
subgraph = G.subgraph(odd_degree_nodes)
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add matching edges to the MST
mst.add_edges_from(matching)

# Convert the graph to Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit into a single tour (Hamiltonian path) by removing repeated visits
visited = set()
tour = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        tour.append(v)
        visited.add(v)

# Calculate the total cost of the tour
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")