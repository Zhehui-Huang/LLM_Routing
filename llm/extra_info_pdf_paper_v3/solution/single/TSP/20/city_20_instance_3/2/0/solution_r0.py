import math
import networkx as nx

# Given cities and their coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25),
    11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Complete graph
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = euclidean_distance(i, j)

# Create a Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G)

# Find vertices with odd degree in the MST to get subgraph for perfect matching
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]
odd_subgraph = G.subgraph(odd_degree_nodes)
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Add matching edges to MST
mst.add_edges_from(matching)

# Create an Eulerian circuit from the enhanced MST
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to a Hamiltonian circuit (simple path, visiting each vertex exactly once)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # to return to the depot

# Calculate the total travel cost
total_cost = sum(euclidean_distance(hamiltonian_circuit[i], hamiltonian_circuit[i + 1]) for i in range(len(hamiltonian_circuit) - 1))

# Output the result
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)