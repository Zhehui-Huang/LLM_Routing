import networkx as nx
import numpy as np
from itertools import combinations

# Define the cities and their coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Creating a complete graph
G = nx.Graph()
for i, coords1 in cities.items():
    for j, coords2 in cities.items():
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(coords1, coords2))

# 1: Compute a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G)

# 2: Find the nodes with the odd degree in the MST
odd_degree_nodes = [node for node in mst.nodes() if mst.degree(node) % 2 == 1]

# 3: Find the minimum weight perfect matching for nodes with odd degree
odd_node_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_node_subgraph, maxcardinality=True)

# 4: Add the edges from the matching to the MST
mst.add_edges_from(min_weight_matching)

# 5: Find an Eulerian circuit in the MST which has all nodes with even degree now
eulerian_circuit = list(nx.eulerian_circuit(mst))

# 6: Convert Eulerian circuit to Hamiltonian circuit, removing repeated nodes
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # return to the starting point

# Calculate the tour cost
total_travel_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the final results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)