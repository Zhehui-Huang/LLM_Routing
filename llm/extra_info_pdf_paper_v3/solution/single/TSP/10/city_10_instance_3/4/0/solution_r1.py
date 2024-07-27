import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

# Define the coordinates of the cities
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
    9: (6, 76)
}

# Calculate distance matrix using Euclidean distance
coords = np.array(list(cities.values()))
dist_matrix = distance_matrix(coords, coords)

# Create graph using NetworkX
G = nx.Graph()
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Compute the minimum spanning tree
mst = nx.minimum_spanning_tree(G)

# Find odd degree nodes in the MST
odd_degree_nodes = [n for n in mst.nodes if mst.degree(n) % 2 == 1]
subgraph = G.subgraph(odd_degree_nodes)

# Calculate minimum-cost perfect matching
row_ind, col_ind = linear_sum_assignment(distance_matrix(coords[odd_degree_nodes], coords[odd_degree_nodes]))
matching = [(odd_degree_nodes[row_ind[i]], odd_degree_nodes[col_ind[i]]) for i in range(len(row_ind))]

# Add edges from the perfect matching to the MST
for u, v in matching:
    if not mst.has_edge(u, v):
        mst.add_edge(u, v, weight=dist_matrix[u][v])

# Create an Eulerian circuit
euler_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert the Eulerian circuit to a Hamiltonian path (shortcutting)
tour = [0]
visited = set([0])
for u, v in euler_circuit:
    if v not in visited:
        tour.append(v)
        visited.add(v)
tour.append(0)  # return to the starting node

# Calculate total cost of the tour
total_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Print result
print("Tour:", tour)
print("Total travel cost:", total_cost)