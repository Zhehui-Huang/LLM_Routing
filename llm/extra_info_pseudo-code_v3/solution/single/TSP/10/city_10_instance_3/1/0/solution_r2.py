import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Coordinates of the cities
coordinates = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28),
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]

# Calculate Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Create a complete graph from the distance matrix
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute a minimum spanning tree (MST) of G
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in T
vertices_odd_degree = [v for v in T.nodes if T.degree(v) % 2 == 1]

# Step 3: Minimum-weight perfect matching on the subgraph induced by odd degree vertices
subgraph_odd = G.subgraph(vertices_odd_degree)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph_odd, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit (skipping repeated vertices)
visited = set()
hamiltonian_circuit = [0]  # Start the tour at the depot
travel_cost = 0
prev_node = 0  # Start from the depot city

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        if v != 0: 
            visited.add(v)
        travel_cost += dist_matrix[prev_node][v]
        hamiltonian_circuit.append(v)
        prev_node = v

# Ensure the tour returns to the depot
if hamiltonian_circuit[-1] != 0:
    travel_cost += dist_matrix[prev_node][0]
    hamiltonian_circuit.append(0)

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {travel_cost}")