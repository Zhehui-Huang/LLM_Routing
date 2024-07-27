import numpy as np
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment
import networkx as nx

# All provided city coordinates
coordinates = np.array([
    (54, 87), (21, 84), (69, 84), (53, 40),
    (54, 42), (36, 30), (52, 82), (93, 44),
    (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
])

# Calculate the Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Create a complete graph with distances as weights
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G, weight="weight")

# Step 2: Find vertices with odd degree in MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Step 3: Minimum-weight perfect matching in the subgraph induced by odd-degree vertices
odd_subgraph = mst.subgraph(odd_degree_nodes)
odd_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Step 4: Create the multigraph by combining edges of MST and odd_matching
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(odd_matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # To return to the starting node

# Calculate total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")