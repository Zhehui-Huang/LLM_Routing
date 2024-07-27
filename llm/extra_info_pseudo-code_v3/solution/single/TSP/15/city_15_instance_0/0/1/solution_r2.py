import numpy as np
import networkx as nx
from itertools import combinations

# Define the cities and their coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Compute Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return np.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Create a complete graph
G = nx.Graph()
for i, j in combinations(cities, 2):
    G.add_edge(i, j, weight=euclidean_distance(i, j))

# 1. Compute minimum spanning tree
mst = nx.minimum_spanning_tree(G, weight='weight')

# 2. Vertices with odd degrees
odd_degree_nodes = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

# 3. Minimum-weight perfect matching among odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, weight='weight', maxcardinality=True)

# Add matched edges to the MST
mst.add_edges_from(min_weight_matching)

# 4. and 5. Find Eulerian circuit in MST with matched edges
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# 6. Convert Eulerian circuit to Hamiltonian circuit (visited control)
hamiltonian_circuit = []
visited = set()
for v, _ in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # complete the tour by including the start node

# Calculate total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Print results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(total_cost, 2))