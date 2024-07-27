import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from itertools import combinations

# City coordinates with depot city at index 0.
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Step 1: Compute distances between each pair of cities
def calculate_distances(coords):
    n = len(coords)
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i, j] = euclidean(coords[i], coords[j])
    return dist

distances = calculate_distances(coords)

# Step 2: Create graph and compute MST
G = nx.complete_graph(len(coords))
for i, j in combinations(range(len(coords)), 2):
    G.edges[i, j]['weight'] = distances[i][j]

mst = nx.minimum_spanning_tree(G)

# Step 3: Find vertices with odd degree in MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Step 4: Minimum Weight Perfect Matching on subgraph induced by odd-degree vertices
odd_subgraph = nx.Graph(mst.subgraph(odd_degree_nodes))
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Step 5: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(mst)
H.add_edges_from(min_weight_matching)

# Step 6: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 7: Convert Eulerian to Hamiltonian circuit
visit_order = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        visit_order.append(u)
        visited.add(u)
visit_order.append(visit_order[0])  # to complete the circuit back to the depot

# Step 8: Calculate total travel cost
total_cost = sum(distances[visit_order[i]][visit_order[i + 1]] for i in range(len(visit_order) - 1))

# Output the result
print("Tour:", visit_order)
print("Total travel cost:", total_cost)