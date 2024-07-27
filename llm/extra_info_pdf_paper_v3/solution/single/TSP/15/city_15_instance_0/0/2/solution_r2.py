import math
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

# Coordinates of the cities (including the depot)
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Calculate the Euclidean distance matrix
dist_matrix = squareform(pdist(cities, metric='euclidean'))

# Function to find odd degree vertices from the MST
def find_odd_vertices(mst):
    odd_vertices = []
    degrees = np.sum(mst != 0, axis=1)
    for index, degree in enumerate(degrees):
        if degree % 2 == 1:
            odd_vertices.append(index)
    return odd_vertices

# Creating Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(dist_matrix)
mst = mst_matrix.toarray()
mst[mst > 0] = 1  # Normalize to simple edges

# Finding vertices with odd degree from the MST
odd_vertices = find_odd_vertices(mst)

# Calculate minimum-cost perfect matching (MCPM) on the subgraph of odd-degree vertices
sub_dist_matrix = dist_matrix[np.ix_(odd_vertices, odd_Vertices)]
sub_mst = minimum_spanning_tree(sub_dist_matrix)
mcpm_matrix = csr_matrix(sub_mst)

# Add the MCPM to the MST to get a graph with all even degree
augmented_matrix = mst.copy()
for ix in range(len(odd_vertices)):
    for jx in range(ix + 1, len(odd_vertices)):
        if sub_mst[ix, jx] > 0:
            i, j = odd_vertices[ix], odd_vertices[jx]
            augmented_matrix[i, j] = augmented_matrix[j, i] = 1

# Find the Eulerian Tour in the augmented graph
def find_eulerian_tour(start, graph):
    num_vertices = len(graph)
    visited = set()
    tour = []

    def visit(vertex):
        stack = [vertex]
        while stack:
            v = stack[-1]
            neighbors = np.where(graph[v] > 0)[0]
            if neighbors.size > 0:
                u = neighbors[0]
                stack.append(u)
                graph[v, u] = graph[u, v] = 0  # remove the edge
            else:
                stack.pop()
                tour.append(v)

    visit(start)  # Start from any vertex
    return tour[::-1]

# Get the Eulerian tour
eulerian_tour = find_eulerian_tour(0, augmented_matrix)

# Convert Eulerian tour to Hamiltonian circuit (remove repeated nodes)
visited = set()
hamiltonian_circuit = []
for city in eulerian_tour:
    if city not in visited:
        visited.add(city)
        hamiltonian_circuit.append(city)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Complete the tour

# Calculate the cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)