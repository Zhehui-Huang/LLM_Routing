import numpy as np
import networkx as nx
from itertools import combinations
import matplotlib.pyplot as plt

# Coordinates
coordinates = np.array([
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
])

# Compute Euclidean Distance
def euclidean_dist(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Graph
num_cities = coordinates.shape[0]
G = nx.complete_graph(num_cities)

# Set edge weights based on Euclidean distances
for u, v in G.edges():
    G[u][v]['weight'] = euclidean_dist(coordinates[u], coordinates[v])

# Step 1: Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')
assert len(list(mst.nodes)) == num_cities, "The MST doesn't include all cities"

# Step 2: Find vertices with odd degree in MST
odd_degree_nodes = [v for v, degree in mst.degree() if degree % 2 == 1]

# Step 3: Minimum weight perfect matching in the subgraph induced by odd-degree nodes
odd_graph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Step 4: Multigraph including MST and minimum matching
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in the multigraph
eulerian_circuit = list(nx.eulerian_circuit(multi_graph))

# Step 6: Making it a Hamiltonian circuit (not necessarily minimal)
visited = set()
hamiltonian_circuit = []

for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Adding depot to complete the tour
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the total cost of the tour
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)