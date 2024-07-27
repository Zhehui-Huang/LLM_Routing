import math
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

# Define the cities' coordinates
positions = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73),
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30),
    (70, 95), (29, 64), (32, 79)
]

# Calculate pairwise Euclidean distances
dist_matrix = distance_matrix(positions, positions)

# Create a complete graph
G = nx.complete_graph(len(positions))
for i in range(len(dist_matrix)):
    for j in range(len(dist_matrix)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Obtain the Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices of odd degree
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Form the subgraph of vertices with odd degree
subgraph = G.subgraph(odd_degree_nodes)
dist_subgraph_matrix = nx.to_numpy_array(subgraph)
row_ind, col_ind = linear_sum_assignment(dist_subgraph_matrix)

# Add minimum weight matching edges to MST
for i, j in zip(row_ind, col_ind):
    if j >= i:
        mst.add_edge(odd_degree_nodes[i], odd_degree_nodes[j], weight=dist_subgraph_matrix[i][j])

# Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(nx.MultiGraph(mst), source=0))

# Convert Eulerian circuit to Hamiltonian path (shortcut method)
path = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        path.append(u)
        visited.add(u)
path.append(0)  # to return to depot

# Calculate total travel cost
total_cost = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))

# Display final results
print(f"Tour: {path}")
print(f"Total travel cost: {total_quest if provided}")