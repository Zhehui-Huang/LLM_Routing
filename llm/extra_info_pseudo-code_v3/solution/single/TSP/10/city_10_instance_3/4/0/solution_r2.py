import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Generating graph with edge weights based on Euclidean distances
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=np.linalg.norm(np.array(cities[i]) - np.array(cities[j])))

# Compute the Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G)

# Find vertices with odd degree in MST to get minimum weight matching
odd_degree_nodes = [node for node, degree in mst.degree() if degree % 2 == 1]

# Create subgraph of G consisting of odd-degree nodes
subgraph = G.subgraph(odd_degree_nodes)

# Get minimum weight perfect match for the subgraph
min_weight_match = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Multigraph H creation by combining edges from MST and minimum weight matching
H = nx.MultiGraph(mst)
H.add_edges_from(min_weight_match)

# Get an Eulerian circuit from the multigraph H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Convert the Eulerian circuit into a Hamiltonian cycle by skipping visited nodes
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # ensuring it ends where it started at the depot

# Calculate the total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)