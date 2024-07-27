import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from networkx import Graph, eulerian_circuit
import networkx.algorithms.matching as nx_matching

# Step 0: Define the cities' coordinates
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]
n = len(cities)

# Step 1: Calculate distances (Euclidean distances here)
def calculate_distances(cities):
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distances[i][j] = euclidean(cities[i], cities[j])
    return distances

distances_matrix = calculate_distances(cities)

# Step 2: Compute minimum spanning tree (MST)
dist_matrix = csr_matrix(distances_matrix)
mst = minimum_spanning_tree(dist_matrix).toarray()

# Step 3: Identify odd degree vertices
odd_vertex = []
degrees = np.sum(np.ceil(mst), axis=1) + np.sum(np.ceil(mst), axis=0)  # Sum rows and columns to get the degree
for i in range(n):
    if int(degrees[i]) % 2 != 0:
        odd_vertex.append(i)

# Step 4: Minimum-weight perfect matching for the odd-degree vertices
induced_subgraph = np.zeros((len(odd_vertex), len(odd_vertex)))
for i, ind in enumerate(odd_vertex):
    for j, jnd in enumerate(odd_vertex):
        induced_subgraph[i, j] = distances_matrix[ind, jnd]

G = Graph()
for idx in range(len(odd_vertex)):
    for jdx in range(idx + 1, len(odd_vertex)):
        G.add_edge(odd_vertex[idx], odd_vertex[jdx], weight=induced_subgraph[idx, jdx])

matching = nx_matching.min_weight_matching(G, maxcardinality=True)

# Adding matching edges to MST
for edge in matching:
    mst[edge[0], edge[1]] = distances_matrix[edge[0], edge[1]]
    mst[edge[1], edge[0]] = distances_matrix[edge[1], edge[0]]

# Step 5: Create Eulerian circuit
multi_graph = Graph(mst)
euler_circ = list(eulerian_circuit(multi_graph, source=0))

# Step 6: Convert Eulerian to Hamiltonian circuit and calculate cost
visited = set()
hamiltonian_circuit = [0]
total_cost = 0
current_node = 0

for u, v in euler_circ:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        total_cost += distances_matrix[current_node, v]
        current_node = v
        visited.add(v)

# Ensuring to return to the starting point
total_cost += distances_matrix[current_node, 0]
hamiltonian_circuit.append(0)

print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")