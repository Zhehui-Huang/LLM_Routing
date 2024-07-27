import math
from itertools import combinations
import networkx as nx
from scipy.spatial import distance_matrix

# Cities coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean distance matrix
coords = list(cities.values())
distance_matrix = distance_matrix(coords, coords)

# Create a graph
G = nx.Graph()

# Add edges with weights
for i, j in combinations(cities.keys(), 2):
    G.add_edge(i, j, weight=distance_matrix[i][j])

# Find Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find nodes with odd degree to perform minimum cost perfect matching
odd_degree_nodes = [v for v in mst.nodes if mst.degree(v) % 2 != 0]

# Generate Minimum Cost Perfect Matching subgraph on Graph with odd degree nodes
min_cost_match_graph = nx.Graph()
min_cost_match_graph.add_nodes_from(odd_degree_nodes)

for u, v in combinations(odd_degree_nodes, 2):
    min_cost_match_graph.add_edge(u, v, weight=distance_matrix[u][v])

# Finding the minimum weight matching
min_cost_matching = nx.algorithms.matching.min_weight_matching(min_cost_match_graph, True)

# Combine the MST and the minimum-cost perfect matching
combined_graph = nx.Graph(mst)
combined_graph.add_edges_from(min_cost_matching)

# Generate the Eulerian circuit from the combined graph
eulerian_circuit = list(nx.eulerian_circuit(combined_graph, source=0))

# Convert Eulerian circuit to Hamiltonian circuit by skipping visited nodes (shortcutting)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)

# Ensure to return to the starting node (depot)
if hamiltonian_circuit[-1] != hamiltonian_circuit[0]:
    hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculating total travel cost
total_travel_cost = sum(distance_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)