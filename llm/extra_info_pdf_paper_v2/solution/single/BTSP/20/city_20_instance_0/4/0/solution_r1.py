import numpy as np
import networkx as nx
from scipy.spatial import distance

# City coordinates as given
coordinates = np.array([
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
])

# Compute the distance matrix using Euclidean distance
def calculate_distances(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i, j] = distance.euclidean(coords[i], coords[j])
    return dist_matrix

dist_matrix = calculate_distances(coordinates)

# Create the graph
def create_complete_graph(dist_matrix):
    G = nx.Graph()
    for i in range(len(dist_index)):
        for j in range(i + 1, len(dist_matrix)):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

G = create_complete_graph(dist_matrix)

# Find the minimum spanning tree
mst = nx.minimum_spanning_tree(G)

# Find nodes of odd degree in the MST
odd_nodes = [node for node in mst.nodes if mst.degree(node) % 2 == 1]
odd_node_subgraph = G.subgraph(odd_nodes)
odd_matching = nx.algorithms.matching.min_weight_matching(odd_node_subgraph, maxcardinality=True)

# Add the matching edges to the MST
mst.add_edges_from(odd_matching)

# Finding a Eulerian circuit
euler_circuit = list(nx.eulerian_circuit(mst, source=0))

# Making the circuit into a path (removing repeated nodes and forming a valid tour)
tour = [euler_circuit[0][0]]
for u, v in euler_circuit:
    if v not in tour:
        tour.append(v)

# Make sure to return to the start point
if tour[0] != tour[-1]:
    tour.append(tour[0])

# Calculate tour cost and maximum distance between consecutive cities
total_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
max_distance = max(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Print outputs
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)