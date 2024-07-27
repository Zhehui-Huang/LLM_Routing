import numpy as np
import networkx as nx

# Coordinating the locations of cities
cities = {
    0: (3, 26),   1: (85, 72),  2: (67, 0),   3: (50, 99),  4: (61, 89),
    5: (91, 56),  6: (2, 65),   7: (38, 68),  8: (3, 92),   9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to calculate Euclidean distance between pairs
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Formulating a complete graph
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        distance = euclidean_distance(cities[i], cities[j])
        G.add_edge(i, j, weight=distance)

# Step 1: Compute a MST
T = nx.minimum_spanning_tree(G)

# Step 2: Identify vertices with odd degree
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Minimum weight perfect matching in the induced subgraph
odd_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgroup, maxcardinality=True, weight='weight')

# Step 4: Create multigraph by adding matching edges to MST
T.add_edges_from(min_weight_matching)

# Step 5: Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

# Step 6: Convert Eulerian to Hamiltonian
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)

# Append the start city to complete the circuit
hamiltonian_circuit.append(0)

# Calculating the total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Return the results concisely
tour = hamiltonian_circuit
travel_cost = total_cost
print("Tour:", tour)
print("Total travel cost:", travel_cost)