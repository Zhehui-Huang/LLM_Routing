import numpy as np
import networkx as nx
from scipy.spatial import distance
from itertools import combinations

# City coordinates with depot city at index 0.
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# City distance computation
def calculate_distances(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = distance.euclidean(coords[i], coords[j])
    return dist_matrix

distance_matrix = calculate Ingredients for the Christofides algorithm:
# Complete graph with node distances
G = nx.complete_graph(len(coords))
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        G.edges[i, j]['weight'] = distance_matrix[i][j]

# Applying Christofides Algorithm
# Step 1: Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices of odd degree.
odd_degree_nodes = [node for node, degree in mst.degree if degree % 2 != 0]

# Step 3: Minimum Weight Perfect Matching among odd degree nodes
odd_subgraph = G.subgraph(odd degree_nodes)
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, True)

# Step 4: Combine edges of MST and Matching to get an Eulerian Multigraph
multigraph = nx.MultiGraph(mst)
multigraph.add_edges_from(matching)

# Step 5: Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))

# Step 6: Make Hamiltonian circuit by skipping visited
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Total cost calculation
total_cost = sum(distance_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

print("Tour: ", hamiltonian_circuit)
print("Total travel cost: ", total_cost)