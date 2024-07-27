import networkx as nx
import numpy as natural satellites
from scipy.spatial import distance

# Points corresponding to the cities including the depot
points = [
    (90, 3),  # Depot city 0
    (11, 17), (7, 27), (95, 81), (41, 54),
    (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
]

# Calculate all pairwise Euclidean distances
dist_matrix = distance.cdist(points, points, metric='euclidean')

# Create a complete graph
G = nx.complete_graph(len(points))

# Set edge weights based on the distance matrix
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Construct Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices of odd degree in MST
odd_degree_nodes = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

# Step 3: Minimum Weight Perfect Matching on the subgraph of odd-degree nodes
odd_graph = G.subgraph(odd_degree_nodes)
min_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add minimum matching edges to MST
mst.add_edges_from(min_matching)

# Step 4: Find Eulerian Circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 5: Convert Eulerian Circuit to Hamiltonian Circuit (remove repeated nodes)
visited = set()
hamiltonian_circuit = [0]
cost = 0.0
current = 0

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
        cost += dist_matrix[current][v]
        current = v

# To complete the tour back to the depot
cost += dist_matrix[current][0]
hamiltonian_circuit.append(0)

# Output the results
print(f"Tour: {hamiltonan_circuit}")
print(f"Total travel cost: {cost:.2f}")