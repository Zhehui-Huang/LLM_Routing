import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean distance matrix
coords = np.array(list(cities.values()))
dist_matrix = squareform(pdist(coords, metric='euclidean'))

# Create a complete graph with distances as weights
G = nx.complete_graph(len(cities))
for i, j in combinations(cities, 2):
    G[i][j]['weight'] = dist_matrix[i][j]

# 1. Compute a minimum spanning tree (MST) of G
T = nx.minimum_spanning_tree(G, weight='weight')

# 2. Identify the set O of vertices with odd degree in T
O = [v for v in T.nodes if T.degree[v] % 2 == 1]

# Create subgraph induced by vertices with odd degree
G_odd = G.subgraph(O)

# 3. Find a minimum-weight perfect matching M in the subgraph induced by O
M = nx.algorithms.matching.min_weight_matching(G_odd, maxcardinality=True, weight='weight')

# 4. Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# 5. Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# 6. Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # return to the start point

# Compute the total travel cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Output the tour and total cost
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")