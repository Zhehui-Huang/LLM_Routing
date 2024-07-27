import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist
from itertools import combinations

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Helper function to calculate the euclidean distance between cities
def distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Creating a complete graph with the cities
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(cities[i], cities[j]))

# Step 1: Compute Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in T
O = [v for v in T if T.degree(v) % 2 == 1]

# Step 3: Minimum-weight perfect matching in the subgraph induced by O
O_subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(O_subgraph, maxcardinality=True)

# Step 4: Add edges of minimum weight matching M to T
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.algorithms.eulerian_circuit(H))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit
hamiltonian_circuit = []
visited = set()
for u, _ in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Adding back the starting node to complete the circuit

# Calculate total travel cost
total_cost = sum(distance(cities[hamiltonian_circuit[i]], cities[hamiltonian_circuit[i+1]]) for i in range(len(hamiltonian_circuit) - 1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)