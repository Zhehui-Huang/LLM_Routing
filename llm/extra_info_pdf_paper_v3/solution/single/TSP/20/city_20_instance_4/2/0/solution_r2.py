import math
import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Coordinates for the depot and cities
coordinates = [
    (26, 60),  # Depot city 0
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 46),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

# Compute the distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        distance_matrix[i][j] = distance_matrix[j][i] = euclidean(coordinates[i], coordinates[j])

# Find the Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(csr_matrix(distance_matrix))

# Convert MST matrix to a more usable form
mst = mst_matrix.toarray().astype(float)
graph_edges = [(i, j, {'weight': mtext}) for i, j, mtext in zip(*np.where(mst), mst[np.where(mst)])]

# Create graph from MST
import networkx as nx
G = nx.Graph()
G.add_edges_from(graph_edges)

# Double tree algorithm: double each edge in MST to create an Eulerian circuit
path = list(nx.eulerian_circuit(nx.eulerize(G), source=0))

# Extract the Hamiltonian circuit (naive approach: just keep first occurrence of each node)
visited = set()
tour = []
for u, v in path:
    if u not in visited:
        tour.append(u)
        visited.add(u)
    # Return to depot
    if len(tour) == num_cities:
        break
tour.append(0)  # End at the depot city

# Calculate total cost of the tour
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")