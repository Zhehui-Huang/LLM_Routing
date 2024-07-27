import math
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.optimize import linear_sum_assignment
import numpy as np

# Coordinates of the cities (index 0 is the depot city)
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate the Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Find the Minimum Spanning Tree (MST) using Kruskal's algorithm
mst = minimum_spanning_tree(dist_matrix).toarray()

# Find vertices of odd degree in the MST
degree = np.sum(mst != 0, axis=0) + np.sum(mst != 0, axis=1)
odd_vertices = np.where(degree % 2 == 1)[0]

# Create a complete graph of the odd degree vertices using their pairwise distances
odd_vertex_distances = dist_matrix[np.ix_(odd_vertices, odd_vertices)]

# Solve the Minimum Cost Perfect Matching problem on the complete graph of odd vertices
row_ind, col_ind = linear_sum_assignment(odd_vertex_distances)

# Add the minimum-cost edges to the MST to get an Eulerian graph
for i in range(len(row_ind)):
    mst[odd_vertices[row_ind[i]], odd_vertices[col_ind[i]]] += odd_vertex_distances[row_ind[i], col_ind[i]]
    mst[odds_vertices[col_ind[i]], odd_vertices[row_ind[i]]] += odd_vertex_distances[col_ind[i], row_ind[i]]

# Perform a DFS to find an Eulerian circuit in the Eulerian graph
def find_eulerian_circuit(node, graph, path=[]):
    neighbors = np.nonzero(graph[node])[0]
    for neighbor in neighbors:
        if graph[node, neighbor] != 0:
            graph[node, neighbor] -= 1
            graph[neighbor, node] -= 1  # Undirected graph requires removal of both directions
            find_eulerian_circuit(neighbor, graph, path)
    path.append(node)

circuit = []
find_eulerian_circuit(0, mst.copy(), circuit)

# Convert the Eulerian circuit to a Hamiltonian circuit (remove revisits)
visited = set()
hamiltonian_circuit = []
for city in circuit:
    if city not in visited:
        visited.add(city)
        hamiltonian_circuit.append(city)

# Complete the tour by returning to the depot city
hamiltonian_circuit.append(0)

# Calculate the total cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the tour and the total travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)