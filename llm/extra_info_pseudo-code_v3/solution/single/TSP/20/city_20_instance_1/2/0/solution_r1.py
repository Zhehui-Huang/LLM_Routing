import numpy as np
import networkx as nx
from itertools import combinations

# Define cities
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Create a function to calculate Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a complete graph with cities as nodes
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Compute the Minimum Spanning Tree (MST) of the graph
mst = nx.minimum_spanning_tree(G)

# Identify vertices with an odd degree in the MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Create subgraph induced by odd degree vertices
odd_graph = G.subgraph(odd_degree_nodes)

# Minimum weight perfect matching in the subgraph of odd-degree vertices
matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Combine edges of MST and minimum weight perfect matching to form a multigraph
H = nx.MultiGraph(mst)
H.add_edges_from(matching)

# Find an Eulerian circuit in the multigraph
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Convert the Eulerian circuit to a Hamiltonian circuit, skipping repeated vertices
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Ensure the tour finishes back at the depot
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate the total travel cost of the tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")