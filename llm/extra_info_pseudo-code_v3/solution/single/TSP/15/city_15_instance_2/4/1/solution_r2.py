import networkx as nx
import numpy as np
from scipy.spatial.distance import cdist

# City coordinates
coords = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Calculating the Euclidean distance matrix
dist_matrix = cdist(coords, coords, metric='euclidean')

# Generating the graph with nodes and weighted edges based on the distance matrix
G = nx.complete_graph(len(coords))
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Construct Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with an odd degree in the MST
odd_degree_nodes = [v for v, degree in mst.degree() if degree % 2 == 1]

# Step 3: Find minimum weight perfect matching on the subgraph induced by odd degree nodes
odd_subgraph = G.subgraph(odd_degree_nodes)
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Step 4: Add the matching edges to the MST to form an Eulerian multigraph
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(matching)

# Step 5: Find an Eulerian circuit in the multigraph
euler_circuit = list(nx.eulerian_circuit(multi_graph))

# Step 6: Form a Hamiltonian circuit by skipping repeated nodes
visited = set()
hamiltonian_circuit = []
total_cost = 0
prev_node = None

for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
        if prev_node is not None:
            total_cost += dist_matrix[prev_node][u]
        prev_node = u

# Closing the circuit by returning to the starting node
hamiltonian_circuit.append(hamiltonian_circuit[0])
total_cost += dist_matrix[prev_node][hamiltonian_circuit[0]]

# Outputting the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(total_cost, 2))