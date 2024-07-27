import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx

# Coordinates of cities including the depot
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]
n = len(cities)

# Step 1: Distance matrix calculation
def calculate_distances(cities):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

distances = calculate_distances(cities)

# Step 2: Compute minimum spanning tree
sparse_dist_mat = csr_matrix(distances)
mst_mat = minimum_spanning_tree(sparse_dist_mat).toarray()

# Step 3: Identify vertices with odd degrees in the MST
degree = np.sum(mst_mat != 0, axis=0) + np.sum(mst_mat != 0, axis=1)
odd_vertices = np.where(degree % 2 != 0)[0]

# Step 4: Minimum-weight perfect matching on odd-degree vertices
odd_graph = nx.Graph()
odd_graph.add_weighted_edges_from(
    (i, j, distances[i][j]) for i in odd_vertices for j in odd Cardinality=True)

matching_weights = nx.min_weight_matching(odd_graph, maxcardinality=True)

# Combine MST and matching to make graph Eulerian
eulerian_graph = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        if mst_mat[i][j] > 0:
            eulerian_graph.add_edge(i, j, weight=distances[i][j])

for edge in matching_weights:
    u, v = edge
    eulerian_graph.add_edge(u, v, weight=distances[u][v])

# Step 5: Find an Eulerian circuit
eulerian_tour = list(nx.eulerian_circuit(eulerian_graph, source=0))

# Step 6: Convert Eulerian circuit to a Hamiltonian circuit (shortcutting)
visited = set()
hamiltonian_circuit = []
current_city = 0
total_distance = 0
for (u, v) in eulerian_tour:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)
        total_distance += distances[u][v]
        current_city = v

# Ensuring first city is the starting point
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)
    total_distance += distances[current_city][0]

# Output results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_distance}")