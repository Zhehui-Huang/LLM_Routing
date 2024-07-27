import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from networkx.algorithms import matching, approximation
from itertools import combinations

# Coordinates of the cities including the depot
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Creating the complete graph
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])

# Step 1: Compute a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices with odd degree in MST
odd_degree_vertices = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

# Step 3: Minimum-weight perfect matching in the induced subgraph on vertices with odd degree
odd_graph = G.subgraph(odd_degree_vertices)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Add the minimum weight matching edges to the MST
mst.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in the augmented graph (MST + M)
eulerian_circuit = list(nx.eulerian_circuit(mst))

# Step 6: Convert Eulerian circuit to Hamiltonian path (skip repeated vertices)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
# Include the last city to complete the circuit
if eulerian_circuit[-1][1] not in visited:
    hamiltonian_circuit.append(eulerian_circuit[-1][1])

# Include back to depot
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Compute total cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)