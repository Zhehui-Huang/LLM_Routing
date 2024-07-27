import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

# Define the coordinates of each city
cities_coords = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Generate a matrix of Euclidean distances between each pair of cities
city_indices = list(cities_coords.keys())
coord_array = np.array([cities_coords[i] for i in city_indices])
distance_matrix = squareform(pdist(coord_array, metric='euclidean'))

# Construct a complete graph with cities as nodes
G = nx.complete_graph(len(city_indices))
for i, j in combinations(city_indices, 2):
    G[i][j]['weight'] = distance_matrix[i][j]

# Generate a minimum spanning tree (MST) from the complete graph
T = nx.minimum_spanning_tree(G, weight='weight')

# Identify vertices in T with odd degrees to find the set O
vertices_odd_degree = [n for n in T.nodes() if T.degree(n) % 2 == 1]

# Form a subgraph using vertices with odd degrees
subgraph_odd = G.subgraph(vertices_odd_degree)

# Find the minimum weight matching for the subgraph with odd degree vertices
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph_odd, maxcardinality=True, weight='weight')

# Construct a multigraph by combining the edges of T and min_weight_matching
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Find an Euler circuit in the multigraph H
euler_circuit = list(nx.eulerian_circuit(H))

# Construct a Hamiltonian circuit from the Euler circuit and avoid visiting the same city twice
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Complete the circuit by returning to the start

# Calculate the total travel distance of the Hamiltonian circuit
total_distance = sum(distance_matrix[hamiltonian_circuit[i]][hamiltonian_circus[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Print the resulting tour and the total travel cost of the tour
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_distance:.2f}")