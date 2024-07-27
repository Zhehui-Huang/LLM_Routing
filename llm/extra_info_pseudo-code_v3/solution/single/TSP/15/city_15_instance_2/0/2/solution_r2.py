import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix

# Defining the coordinates of the cities
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Generating a distance matrix using Euclidean distance
dist_matrix = distance_matrix(coordinates, coordinates)

# Creating a complete graph where nodes are cities and edge weights are distances
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute a minimum spanning tree (MST) of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Gather vertices with an odd degree in T
odd_degree_vertices = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Find the minimum weight perfect matching for the odd-degree vertices subgraph
subgraph = G.subgraph(odd_degree_vertices)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Add edges from the minimum-weight perfect matching to T
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in the resulting multigraph H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Create a Hamiltonian circuit from the Eulerian circuit by skipping visited nodes
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Making sure the tour ends at the starting point (depot)
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate the total cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Print the tour and the total travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)