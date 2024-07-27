import networkx as nx
import numpy as np

# Coordinates of the cities
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}


def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


# Create complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G)

# Step 2: Identify the set O of vertices with odd degree in T
odd_degree_nodes = [v for v in T.nodes() if T.degree(v) % 2 != 0]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
odd_subgraph = G.subgraph(odd_degree_nodes)
min_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Step 4: Combine the edges of T and M
H = nx.MultiGraph(T)
H.add_edges_from(min_matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert to Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]  # start at depot
for (u, v) in eulerian_circuit:
    if not v in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # return to depot

# Total cost calculation
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Display the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)