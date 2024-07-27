import math
import networkx as nx
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define the positions of each city on the map
positions = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Step 1: Compute a complete graph G
G = nx.complete_graph(len(positions))
for u, v in G.edges():
    G[u][v]['weight'] = euclidean_distance(positions[u], positions[v])

# Step 2: Compute a minimum spanning tree T of G
T = nx.minimum_spanning_tree(G)

# Step 3: Identify the set O of vertices with odd degree in T
odd_degree_nodes = [v for v, degree in T.degree() if degree % 2 == 1]

# Step 4: Find a minimum-weight perfect matching M in the subgraph induced by O
odd_degree_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_degree_subgraph, maxcardinality=True)

# Add the edges of the matching to the tree
T.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H (here T is now H)
eulerian_circuit = list(nx.eulerian_circuit(T))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = []

for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # add the starting point to end point to complete the circuit

# Calculate total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Print results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(total_cost, 2))