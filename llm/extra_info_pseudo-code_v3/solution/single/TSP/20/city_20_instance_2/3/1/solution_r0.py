import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Define the coordinates of the cities
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49),
    17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Create a function to calculate distance matrix
def compute_distances(cities):
    coords = np.array(list(cities.values()))
    return distance_matrix(coords, coords)

# Step 1: Compute distance matrix
dist_matrix = compute_distances(cities)

# Step 2: Construct complete graph G
G = nx.complete_graph(len(cities))
for i, j in combinations(cities, 2):
    G[i][j]['weight'] = dist_matrix[i, j]

# Step 3: Compute a minimum spanning tree (MST) T
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 4: Identify vertices with odd degree in the MST
odd_degree_nodes = [v for v, degree in mst.degree() if degree % 2 == 1]

# Step 5: Compute minimum-weight perfect matching among odd-degree vertices
odd_degree_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_degree_subgraph, maxcardinality=True, weight='weight')

# Step 6: Construct multigraph by combining MST and the minimum-weight perfect matching
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(min_weight_matching)

# Step 7: Find an Eulerian circuit (This circuit will automatically be a Hamiltonian circuit)
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Step 8: Convert the Eulerian circuit into a Hamiltonian path, skipping visited cities
visited = set()
hamiltonian_circuit = [0]
current_cost = 0

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
        current_cost += dist_matrix[u][v]

# Complete the tour by returning to the starting point
hamiltonian_circuit.append(0)
current_cost += dist_matrix[hamiltonian_circuit[-2]][0]

print(f"Tour: {hamiltonaian_courcuit}")
print(f"Total travel cost: {current_cost}")