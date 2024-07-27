import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx

# Coordinates for cities
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate the distance matrix
dist_matrix = distance_matrix(cities, cities)

# Compute the Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(dist_matrix)
mst_matrix = mst_matrix.toarray()

def get_odd_degree_vertices(mst):
    # Find vertices with odd degree in the MST
    degree = np.sum(mst != 0, axis=0) + np.sum(mst != 0, axis=1)
    odd_vertices = np.where(degree % 2 == 1)[0]
    return odd_vertices

odd_vertices = get_odd_degree_vertices(mst_matrix)

# Create a graph of odd degree vertices
induced_graph = dist_matrix[np.ix_(odd_vertices, odd_vertices)]
graph = nx.Graph()
for i in range(len(odd_vertices)):
    for j in range(len(odd_vertices)):
        if i != j:
            graph.add_edge(i, j, weight=induced_graph[i, j])

# Minimum weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True)

# Adding matching edges to the mst_matrix
for edge in matching:
    i, j = edge[0], edge[1]
    mst_matrix[odd_vertices[i], odd_vertices[j]] = induced_graph[i, j]
    mst_matrix[odd_vertices[j], odd_vertices[i]] = induced_graph[j, i]

# Convert the MST with added matching into a Graph
multi_graph = nx.Graph(mst_matrix)

# Find Eulerian circuit
eulerian_tour = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert Eulerian circuit to a Hamiltonian path
visited = set()
hamiltonian_tour = [0]
visited.add(0)
for u, v in eulerian_tour:
    if v not in visited:
        hamiltonian_tour.append(v)
        visited.add(v)
hamiltonian_tour.append(0)  # Return to the starting city

# Calculate the tour cost
tour_cost = sum(dist_matrix[hamiltonian_tour[i], hamiltonian_tour[i+1]] for i in range(len(hamiltonian_tour) - 1))

# Output the result
print("Tour:", hamiltonian_tour)
print("Total travel cost:", tour_cost)