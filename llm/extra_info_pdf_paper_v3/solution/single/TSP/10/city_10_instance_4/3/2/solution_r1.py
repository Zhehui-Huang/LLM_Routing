import numpy as np
import networkx as nx
from itertools import combinations

# Coordinates of the cities
coordinates = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61),
    (22, 21), (97, 70), (20, 99), (66, 62)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return round(np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))

# Create a complete graph with Euclidean distances as edge weights
G = nx.Graph()
num_cities = len(coordinates)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=euclidean_distance(coordinates[i], coordinates[j]))

# Find the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find vertices with odd degree in the MST
odd_degree_vertices = [v for v in mst.nodes if mst.degree(v) % 2 != 0]

# Create a minimum cost perfect matching to make graph Eulerian
subgraph = G.subgraph(odd_degree_vertices)
min_cost_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add minimum cost matching edges to the MST
mst.add_edges_from(min_cost_matching)

# Find the Eulerian tour
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian tour to Hamiltonian path, visiting each city only once
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Return to the start to complete the circuit
hamiltonian_circuit.append(0)

# Calculate the total cost of the circuit
total_travel_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Provide the output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)