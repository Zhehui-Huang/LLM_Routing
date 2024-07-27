import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist
from networkx.algorithms.approximation import min_weighted_dominating_set

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np2)

# Define cities and coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Create distance matrix
coords = list(cities.values())
distance_mat = cdist(coords, coords)

# Generate a graph from distance matrix
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=distance_mat[i][j])

# Step 1: Minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with an odd degree
odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Minimum-weight perfect matching on odd-degree nodes
odd_degree_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_cie_subgraph, maxcardinality=True)

# Step 4: Combine the edges of T and edges from M to create multi-graph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in the multi-graph H
eulerian_path = list(nx.eulerian_circuit(H))

# Step 6: Make a Hamiltonian circuit from the Eulerian circuit (skip repeated cities)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_path:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Return to the starting point

# Calculate the tour's total cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)