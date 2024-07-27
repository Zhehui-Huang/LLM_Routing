import networkx as nx
import numpy as np
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

# Defining city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Compute distances matrix
coords = np.array(list(cities.values()))
dist_matrix = squareform(pdist(coords, metric='euclidean'))

# Create graph from distance matrix
G = nx.complete_graph(len(cities))
for i, j in combinations(range(len(cities)), 2):
    G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices with odd degree in T
O = [v for v in T.nodes() if T.degree[v] % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # adding the depot city again at the end

# Calculate the total travel cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)