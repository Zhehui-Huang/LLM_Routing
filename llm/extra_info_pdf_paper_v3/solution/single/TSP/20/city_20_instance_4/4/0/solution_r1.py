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

# Number of cities
num_cities = len(cities)

# Step 1: Compute the Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(dist_matrix)
mst_matrix = mst_matrix.toarray()

# Step 2: Find the odd-degree vertices in the MST
degree = np.sum(mst_matrix != 0, axis=0) + np.sum(mst_matrix != 0, axis=1)

# Odd-degree vertices
odd_vertices = np.where(degree % 2 == 1)[0]

# Step 3: Minimum weight perfect matching on the induced subgraph of odd degree vertices
induced_graph = dist_matrix[np.ix_(odd_vertices, odd_vertices)]
graph = nx.Graph()
for i in range(len(odd_vertices)):
    for j in range(i+1, len(odd_vertices)):
        graph.add_edge(odd_vertices[i], odd_vertices[j], weight=induced_graph[i, j])

# Find minimum weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True)

# Enhanced MST with matching
edge_added = lil_matrix(dist_matrix.shape)
for (i, j) in matching:
    mst_matrix[i, j] = dist_matrix[i, j]
    mst_matrix[j, i] = dist_matrix[j, i]
    edge_added[i, j] = 1
    edge_added[j, i] = 1

# Merge the MST and the matching result
final_graph = mst_matrix + edge_added

# Step 4: Finding an Eulerian Tour from the MST + matching
graph = nx.from_numpy_matrix(final_graph, create_using=nx.MultiGraph)
eulerian_tour = list(nx.eulerian_circuit(graph, source=0))

# Convert Eulerian circuit to Hamiltonian circuit by skipping repeated nodes
visited = set()
hamiltonian_tour = [0]  # start from the depot city
visited.add(0)
for (u, v) in eulerian_tour:
    if v not in visited and v != 0:
        hamiltonian_tour.append(v)
        visited.add(v)
hamiltonian_tour.append(0)  # return to the depot city

# Calculate the tour cost
tour_cost = sum(dist_matrix[hamiltonian_tour[i], hamiltonian_tour[i + 1]] for i in range(len(hamiltonian_tour) - 1))

# Output the result
print(f"Tour: {hamiltonian_tour}")
print(f"Total travel cost: {tour_cost}")