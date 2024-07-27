import numpy as np
import networkx as nx
from itertools import combinations
from scipy.spatial import distance_matrix

# Provided coordinates of cities and the depot
coordinates = np.array([
    (90, 3), (11, 17), (7, 27), (95, 81), (41, 54), 
    (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
])

# Step 1: Compute the distance matrix (Euclidean distances)
dist_matrix = distance_matrix(coordinates, coordinates)

# Step 2: Construct a complete graph with distances
G = nx.complete_graph(len(coordinates))
for i, j in G.edges():
    G[i][j]['weight'] = dist_matrix[i][j]

# Step 3: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 4: Identify the set O of vertices with odd degree in T
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Step 5: Find a minimum-weight perfect matching M in the subgraph induced by odd_degree_nodes
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 6: Add the edges from the minimum weight matching to the MST
T.add_edges_from(min_weight_matching)

# Step 7: Find an Eulerian circuit in the updated graph (T)
eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

# Step 8: Convert the Eulerian circuit to a Hamiltonian circuit (by skipping repeated vertices)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    # Add last city manually if it's the first time
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Add the start city (depot city) to complete the circuit
hamiltonian_circuit.append(0)

# Calculate the total travel cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)