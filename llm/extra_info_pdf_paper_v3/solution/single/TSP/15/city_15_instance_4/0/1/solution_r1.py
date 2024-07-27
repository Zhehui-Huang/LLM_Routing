import math
import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.optimize import linear_sum_assignment

# Coordinates of cities, index 0 is the depot
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate the Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Compute the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(dist_matrix).toarray()

# Helper function to find odd degree vertices in MST
def get_odd_degree_vertices(graph):
    degree = np.sum(graph != 0, axis=0) + np.sum(graph != 0, axis=1)
    odd_vertices = np.where(degree % 2 == 1)[0]
    return odd_vertices

# Get all odd-degree vertices in the MST
odd_vertices = get_odd_degree_vertices(mst)

# Create a complete graph for the odd-degree vertices using their pairwise distances
subgraph = dist_matrix[np.ix_(odd_vertices, odd_vertices)]

# Compute the minimum-weight perfect matching on the odd-degree subgraph
row_ind, col_ind = linear_sum_assignment(subnx)

# Add edges to the MST to make it Eulerian
for i in range(len(row_ind)):
    mst[odd_vertices[row_ind[i]], odd_vertices[col_ind[i]]] += 1
    mst[odd_vertices[col_ind[i]], odd_vertices[row_ind[i]]] += 1

# Helper function to find Eulerian circuit from an Eulerian graph starting at node
def eulerian_path(graph, start_node):
    num_vertices = graph.shape[0]
    stack = [start_node]
    path = []

    while stack:
        current_vertex = stack[-1]
        if np.any(graph[current_vertex] > 0):
            next_vertex = np.argmax(graph[current_vertex] > 0)
            graph[current_vertex, next_vertex] -= 1
            graph[next_vertex, current_vertex] -= 1
            stack.append(next_vertex)
        else:
            path.append(stack.pop())
    return path[::-1]

# Find an Eulerian circuit
eulerian_circuit = eulerian_path(mst, 0)

# Convert Eulerian to Hamiltonian circuit (to TSP tour)
visited = set()
hamiltonian_circuit = [0]  # start at the depot
for city in eulerian_circuit:
    if city not in visited:
        visited.add(city)
        hamiltonian_circuit.append(city)

# Ensure we end at the depot
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate the tour cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)