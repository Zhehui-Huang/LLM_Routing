import numpy as np
from scipy.spatial import distance
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx
from itertools import combinations
from networkx.algorithms.matching import max_weight_matching

# Coordinates of cities indexed from 0 to 19
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82), 
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Distance matrix computation
n = len(cities)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i, j] = distance.euclidean(cities[i], cities[j])

# Step 1: Compute MST
t_csr = csr_matrix(dist_matrix)
mst_array = minimum_spanning_tree(t_csr).toarray()

# Convert MST to a graph
mst_graph = nx.Graph()
for i in range(n):
    for j in range(n):
        if mst_array[i, j] > 0:
            mst_graph.add_edge(i, j, weight=mst_array[i, j])

# Step 2: Find vertices with odd degree
odd_degree_nodes = [v for v, d in mst_graph.degree() if d % 2 == 1]

# Step 3: Find minimum weight perfect matching inside odd_vertex_subset
odd_node_subgraph = nx.complete_graph(odd_degree_nodes)
for u, v in odd_node_subgraph.edges():
    odd_node_subgraph[u][v]['weight'] = dist_matrix[u][v]
matching = max_weight_matching(odd_node_subgraph, maxcardinality=True, weight='weight')

# Add matching to the MST
for edge in matching:
    mst_graph.add_edge(edge[0], edge[1], weight=dist_matrix[edge[0]][edge[1]])

# Step 5: Find Eulerian Circuit
eulerian_circuit = list(nx.eulerian_circuit(mst_graph, source=0))

# Step 6: Convert to Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
total_cost = 0
current_node = 0

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        total_cost += dist_matrix[current_node, v]
        current_node = v
        visited.add(v)

# Ensuring it's a tour (return to depot)
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)
    total_cost += dist_matrix[current_node, 0]

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)