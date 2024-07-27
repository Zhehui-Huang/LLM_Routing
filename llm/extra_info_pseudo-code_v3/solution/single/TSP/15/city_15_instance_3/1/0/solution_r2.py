import numpy as np
import networkx as nx
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

# Helper function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Create complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# 1. Compute Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# 2. Identify vertices with odd degree in MST
O = [node for node in T.nodes() if T.degree(node) % 2 == 1]

# 3. Minimum-weight perfect matching in the subgraph induced by O
subgraph_O = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(subgraph_O, maxcardinality=True, weight='weight')

# 4. Combine edges of T and M
H = nx.MultiGraph(T)
H.add_edges_from(M)

# 5. Find an Eulerian Circuit
euler_circuit = list(nx.eulerian_circuit(H))

# 6. Make a Hamiltonian circuit, skipping repeated nodes
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)

# Add the depot back to complete the tour
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculating total cost
total_cost = 0.0
for i in range(len(hamiltonian_circuit)-1):
    total_cost += euclidean_distance(cities[hamiltonian_circuit[i]], cities[hamiltonian_circuit[i+1]])

# Output the results
tour_output = "Tour: " + str(hamiltonian_circuit)
cost_output = "Total travel cost: {:.2f}".format(total_cost)

print(tour_output)
print(cost_output)