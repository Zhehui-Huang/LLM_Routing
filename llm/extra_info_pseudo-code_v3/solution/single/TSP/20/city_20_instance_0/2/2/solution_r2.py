import networkx as nx
import numpy as np
from itertools import combinations

# Definition of cities
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Calculate distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initialize a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Generate Minimum Spanning Tree from the graph
T = nx.minimum_spanning_tree(G)

# Get nodes with odd degree to create O
O = [node for node in T.nodes() if T.degree(node) % 2 == 1]

# Create subgraph induced by O for minimum weight matching
subgraph = G.subgraph(O)
min_weight_match = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Creating the multigraph H by adding edges from T and the minimum weight perfect matching
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_match)

# Finding Eulerian tour
eulerian_tour = list(nx.eulerian_circuit(H))

# Convert Eulerian tour to Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]  # start at the depot
for u, v in eulerian_tour:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)
    if len(visited) == len(cities):  # all cities visited
        break

# Adding depot to complete the circuit
hamiltonian_circuit.append(0)

# Compute total distance
total_cost = sum(distance(hamiltonian_circuit[i], hamiltonian_circuit[i+1]) for i in range(len(hamiltonian_circuit)-1))

# Solution output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(total_cost, 2))