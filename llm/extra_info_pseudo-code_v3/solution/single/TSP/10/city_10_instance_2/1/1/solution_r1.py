import numpy as np
import networkx as nx
from scipy.spatial import distance
from itertools import combinations

# Given city coordinates
cities = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81),
    4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56),
    8: (49, 29), 9: (13, 17)
}

# Step 1: Compute pairwise Euclidean distances for the complete graph
def calculate_distances(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist = distance.euclidean(cities[i], cities[j])
                dist_matrix[i][j] = dist
    return dist_matrix

dist_mx = calculate_distances(cities)

# Create complete graph from distance matrix
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=dist_mx[i][j])

# Step 2: Compute MST
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 3: Find odd degree vertices
odd_vertices = [v for v, d in mst.degree() if d % 2 == 1]

# Step 4: Find minimum weight perfect matching in the induced subgraph on odd vertices
odd_graph = G.subgraph(odd_vertices)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add the matching edges to MST
mst.add_edges_from(min_weight_matching)

# Step 5: Form a multigraph from MST and matching edges, find an Eulerian circuit
multi_graph = nx.MultiGraph(mst)
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert the Eulerian circuit to a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Include the start and end at the depot
hamiltonian_circuit = [0] + hamiltonian_circuit + [0]

# Calculate the total travel cost
tour_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_cutoff[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {tour_cost}")