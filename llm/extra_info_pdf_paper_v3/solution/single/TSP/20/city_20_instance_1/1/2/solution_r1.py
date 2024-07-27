import math
import networkx as nx

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Define the cities and their locations
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

# Create a complete graph for all cities
G = nx.complete_graph(len(cities))

# Add the distances as weights in the graph
for (u, v) in G.edges():
    G[u][v]['weight'] = calculate_address(cities[u], cities[v])

# Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find odd degree vertices in MST
odd_degree_nodes = [n for n in mst.nodes() if mst.degree(n) % 2 == 1]

# Create subgraph of these odd degree vertices
odd_subgraph = G.subgraph(odd_degree_nodes)

# Find minimum weight perfect matching to pair odd degree vertices
match = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Add these matched edges to original MST
mst.add_edges_from(match)

# Form an Eulerian circuit from this augmented graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to Hamiltonian path by skipping repeated nodes
hamiltonian_circuit = [0]  # start at node 0
visited = {0}
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Return to the depot city to complete the circuit
hamiltonian_circuit.append(0)

# Calculate total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)