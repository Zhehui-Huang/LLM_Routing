import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order
from networkx import Graph, eulerian_circuit
from itertools import combinations

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82), 
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23), 
    (78, 76), (68, 45), (50, 28), (69, 9)
]

# Step 1: Calculate distance matrix
distance_mat = distance_matrix(cities, cities)

# Step 2: Construct the MST
mst_matrix = minimum_spanning_tree(csr_matrix(distance_mat))

# Step 3: Find vertices with odd degree in the MST
mst_graph = Graph(mst_matrix)
deg = list(mst_graph.degree)
odd_degree_nodes = [node for node, degree in deg if degree % 2 == 1]

# Step 4: Minimum Cost Perfect Matching on odd degree nodes
subgraph = Graph()
subgraph.add_nodes_from(odd_degree_nodes)
for u, v in combinations(odd_offsets, 2):
    subgraph.add_edge(u, v, weight=distance_mat[u][v])
matching = networkx.algorithms.max_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Combine MST and matching to form the Eulerian circuit
multi_graph = Graph(mst_graph)
multi_graph.add_edges_from(matching)
euler_circuit = list(eulerian_circuit(multi_graph, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit
visited = set()
hamiltonian_path = []
for u, v in euler_circuit:
    if v not in visited:
        hamiltonian_path.append(v)
        visited.add(v)
hamiltonian_path.append(0)  # return to the starting node

# Step 7: Calculate the total travel cost
total_cost = sum(distance_mat[hamiltonian_path[i], hamiltonian_path[i+1]] for i in range(len(hamiltonian_path)-1))

# Output the results
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)