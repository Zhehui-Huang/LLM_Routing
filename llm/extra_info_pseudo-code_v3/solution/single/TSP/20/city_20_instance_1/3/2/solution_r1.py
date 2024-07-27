import math
from scipy.spatial import distance_matrix
import numpy as np
from networkx import Graph, minimum_spanning_tree, eulerian_circuit, set_node_attributes, is_eulerian
from networkx.algorithms.matching import max_weight_matching
from itertools import combinations

# Cities coordinates (city index starts from 0)
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Distance matrix calculation
dist_matrix = distance_matrix(cities, cities)

# Total number of cities
num_cities = len(cities)

# Create a complete graph with all cities
graph = Graph()
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        graph.add_edge(i, j, weight=dist_matrix[i][j])

# Step 1: Compute a Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(graph)

# Step 2: Identify the set O of vertices with odd degree in T
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Create subgraph induced by nodes with odd degree
odd_graph = graph.subgraph(odd_degree_nodes)

# Step 3: Find a minimum-weight perfect matching in the subgraph induced by O
matching = max_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add matching edges to MST
mst.add_edges_from(matching)

# Step 4: Create the multigraph H by combining edges of T and M
# Already combined in previous step
# Ensure the graph has all even degree
assert all(d % 2 == 0 for v, d in mst.degree())

# Step 5: Find an Eulerian circuit in H
if is_eulerian(mst):
    euler_circuit = list(eulerian_circuit(mst, source=0))
else:
    raise Exception("The graph is not Eulerian as expected.")

# Step 6: Convert Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # to return to the start point

# Calculate the total travel cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")