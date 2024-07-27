import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

# Cities coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Creating a complete graph
G = nx.Graph()
for i in range(20):
    for j in range(i + 1, 20):
        G.add_edge(i, j, weight=distance(i, j))

# Step 1: Compute MST T of G
T = nx.minimum_spanning_tree(G)

# Step 2: Set O of odd degree vertices in T
O = [v for v in T.nodes if T.degree(v) % 2 != 0]

# Step 3: Minimum-weight perfect matching M on O
O_subgraph = nx.Graph()
O_subgraph.add_nodes_from(O)
for u, v in combinations(O, 2):
    O_subgraph.add_edge(u, v, weight=distance(u, v))
M = nx.algorithms.matching.min_weight_matching(O_subgraph, maxcardinality=True)

# Step 4: Combine edges of T and M in multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in multigraph H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Creating Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)
    if v == 0:
        break

# Calculate the travel cost
total_travel_cost = sum(distance(hamiltonian_circuit[i], hamiltonian_circuit[i+1]) for i in range(len(hamiltonian_circuit) - 1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)