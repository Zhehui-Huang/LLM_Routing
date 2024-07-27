import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from networkx.algorithms import minimum_spanning_tree
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.euler import eulerian_circuit

# City coordinates (index is the city number)
coordinates = [
    (3, 26),   # Depot 0
    (85, 72),  # 1
    (67, 0),   # 2
    (50, 99),  # 3
    (61, 89),  # 4
    (91, 56),  # 5
    (2, 65),   # 6
    (38, 68),  # 7
    (3, 92),   # 8
    (59, 8),   # 9
    (30, 88),  # 10
    (30, 53),  # 11
    (11, 14),  # 12
    (52, 49),  # 13
    (18, 49),  # 14
    (64, 41),  # 15
    (28, 49),  # 16
    (91, 94),  # 17
    (51, 58),  # 18
    (30, 48)   # 19
]

# Number of Cities
num_cities = len(coordinates)

# Calculate distance matrix
dist_matrix = squareform(pdist(coordinates, metric='euclidean'))

# Create a complete graph from the distance matrix
graph = nx.complete_graph(num_cities)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        graph[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute a minimum spanning tree (MST) T of G
mst = minimum_spanning_tree(graph)

# Step 2: Identify the set O of vertices with odd degree in MST
odd_degree_nodes = [node for node, degree in dict(mst.degree()).items() if degree % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
odd_subgraph = mst.subgraph(odd_degree_nodes)
perfect_matching = nx.Graph(max_weight_matching(odd_subgraph, maxcardinality=True, weight='weight'))
min_weight_matching = nx.Graph()
for edge in perfect_matching.edges():
    min_weight_matching.add_edge(*edge, weight=dist_matrix[edge[0]][edge[1]])

# Step 4: Combine the edges of T and M to form a multigraph H
multigraph = nx.MultiGraph(mst)
for edge in min_weight_matching.edges(data=True):
    multigraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])

# Step 5: Find an Eulerian circuit in H
euler_circuit = list(eulerian_circuit(multigraph))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
for u, v in euler_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Make sure to return to the start point
hamiltonian_circuit.append(0)

# Calculate the total cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Print the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")