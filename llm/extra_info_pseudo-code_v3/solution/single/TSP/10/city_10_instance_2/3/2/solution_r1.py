import numpy as np
from scipy.spatial.distance import pdist, squareform
import networkx as nx
from networkx.algorithms import matching

# Define city coordinates
coordinates = np.array([
    (90, 3),  # Depot city 0
    (11, 17), (7, 27), (95, 81), (41, 54),
    (31, 35), (23, 95), (20, 56), (49, 29),
    (13, 17)  # City 9
])

# Calculate the distance matrix using Euclidean distance
distance_matrix = squareform(pdist(coordinates, 'euclidean'))

# Create a complete graph
G = nx.complete_graph(len(coordinates))
for i in range(len(G.nodes)):
    for j in range(i+1, len(G.nodes)):
        G[i][j]['weight'] = distance_matrix[i][j]

# Step 1: Compute the MST
mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

# Step 2: Find vertices with an odd degree
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 != 0]

# Create a subgraph with these odd degree nodes
odd_graph = G.subgraph(odd_degree_nodes)

# Step 3: Find a minimum-weight perfect matching in the subgraph induced by odd_degree_nodes
min_weight_matching = matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Step 4: Add the matching edges to the MST
mst.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit (skip repeated vertices)
seen = set()
hamiltonian_circuit = []
total_cost = 0
prev_node = None

for u, v in eulerian_circuit:
    if u not in seen:
        hamiltonian_circuit.append(u)
        seen.add(u)
    if prev_node is not None:
        total_cost += G[prev_node][u]['weight']
    prev_node = u
# Complete the tour by going back to the depot, cost calculation included
total_cost += G[prev_node][0]['weight']
hamiltonian_circuit.append(0)

# Results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)