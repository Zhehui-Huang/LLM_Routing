import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from itertools import combinations

# Given cities coordinates
cities = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81),
    4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56),
    8: (49, 29), 9: (13, 17)
}

# Step 1: Calculate pairwise Euclidean distances for the complete graph
def calculate_distances(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean(cities[i], cities[j])
            dist_matrix[i, j] = dist_matrix[j, i] = dist
    return dist_matrix

dist_matrix = calculate_distances(cities)

# Create complete graph from distance matrix
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=dist_mx[i][j])

# Step 2: Compute MST
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 3: Find odd degree vertices
odd_vertices = [v for v, d in mst.degree() if d % 2 == 1]

# Step 4: Compute minimum weight perfect matching on the subgraph induced by odd degree vertices
odd_subgraph = G.subgraph(odd_vertices)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Step 5: Combine MST and minimum-weight perfect matching
mst.add_edges_from(min_weight_matching)

# Step 6: Find an Eulerian circuit in the combined graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 7: Convert to Hamiltonian circuit by skipping visited nodes
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Back to the starting point (depot)
hamiltonian_circuit.append(0)

# Step 8: Calculate tour cost
tour_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {tour_cost}")