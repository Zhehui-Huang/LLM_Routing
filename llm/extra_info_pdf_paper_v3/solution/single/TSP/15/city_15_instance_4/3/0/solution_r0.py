import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Define the cities coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Number of cities
num_cities = len(cities)

# Create distance matrix
coords = np.array(list(cities.values()))
dist_matrix = distance_matrix(coords, coords)

# Create a complete graph from the distance matrix
G = nx.complete_graph(num_cities)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Find the minimum spanning tree
mst = nx.minimum_spanning_tree(G)

# Find all nodes with odd degree in the MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Create subgraph induced by nodes with odd degree
odd_degree_subgraph = G.subgraph(odd_degree_nodes)

# Find minimum weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(odd_degree_subgraph, maxcardinality=True)

# Add matching edges to MST
mst.add_edges_from(matching)

# Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to a Hamiltonian circuit (shortcutting)
visited = set()
tour = [0]
total_distance = 0
current_city = 0

for _, next_city in eulerian_circuit:
    if next_city not in visited:
        visited.add(next_city)
        total_distance += dist_matrix[current_city, next_city]
        tour.append(next_city)
        current_city = next_city

# Going back to the depot
tour.append(0)
total_distance += dist_matrix[current_city, 0]

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_distance)