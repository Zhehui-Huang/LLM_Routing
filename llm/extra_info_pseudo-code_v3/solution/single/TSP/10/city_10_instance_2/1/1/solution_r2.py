import numpy as np
import networkx as nx
from scipy.spatial import distance

# Given city coordinates
cities = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81),
    4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56),
    8: (49, 29), 9: (13, 17)
}

# Compute Euclidean distance matrix for all city pairs
def calculate_distances(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = distance.euclidean(cities[i], cities[j])
            dist_matrix[i, j] = dist_matrix[j, i] = dist
    return dist_matrix

dist_matrix = calculate_distances(cities)

# Create a complete graph with weights equal to distances
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree in the MST
odd_degree_vertices = [v for v, d in mst.degree() if d % 2 == 1]

# Step 3: Create a minimum weight perfect matching for the odd degree vertices
odd_graph = G.subgraph(odd_degree_vertices)
matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Step 4: Combine the MST and the matching to form a multigraph
mst.add_edges_from(matching)

# Step 5: Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Reduce Eulerian circuit to Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Fix if starts and ends not with 0
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the Hamiltonian circuit and the total cost
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")