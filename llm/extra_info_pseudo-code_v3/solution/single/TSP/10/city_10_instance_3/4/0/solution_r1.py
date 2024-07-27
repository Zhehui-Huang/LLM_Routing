import numpy as np
import networkx as nx
from scipy.spatial import distance
from itertools import combinations

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate the Euclidean distance
def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Complete graph creation
G = nx.complete_graph(len(cities))
for i in cities:
    for j in cities:
        if i != j:
            G[i][j]['weight'] = euclideanientes euclidean_distance(cities[i], cities[j]))

# Step 1: Compute Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 2: Identify vertices with odd degree in MST
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Find Minimum Weight Perfect Matching in the subgraph induced by nodes of odd degree
odd_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Step 4: Add edges from the matching to the MST to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian Circui
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert Eulerian to Hamiltonian Path, skipping repeated vertices
visited = set()
hamiltonian_circuit = [0]  # Start at depot city 0
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # Return to the depot city

# Calculate total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)