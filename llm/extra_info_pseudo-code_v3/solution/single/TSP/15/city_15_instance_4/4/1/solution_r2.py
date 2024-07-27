import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms import approximation as approx

# Define the coordinates of the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate the Euclidean distance matrix
dist_matrix = distance_matrix(cities, cities)

# Create a complete weighted graph
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Step 1: Compute a minimum spanning tree (MST) T of G.
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices with odd degree in T.
O = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O.
O_subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(O_subgraph, maxcardinality=True)

# Step 4: Add edges from M to T to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H.
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices.
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Return to the start

# Calculate the total travel cost of the Hamiltonian circuit
total_travel_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit)-1))

# Output the tour and total travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)