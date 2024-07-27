import math
import numpy as np
import networkx as nx
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Cities coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create graph
n = len(cities)
dist_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean_number(cities[i], cities[j])

# Step 1: Compute the MST
mst = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()

# Step 2: Get vertices with odd degree
degree = np.sum(mst != 0, axis=0) + np.sum(mst != 0, axis=1)
odd_vertices = [i for i in range(n) if degree[i] % 2 == 1]

# Step 3: Find minimum weight perfect matching
graph = nx.Graph()
graph.add_weighted_edges_from((i, j, dist_matrix[i][j]) for i in range(n) for j in range(n) if i != j)
min_weight_matching = nx.algorithms.matching.min_weight_matching(graph.subgraph(odd_vertices), maxcardinality=True)

# Form the multigraph
multi_graph = nx.Graph()
for i in range(n):
    for j in range(n):
        if mst[i][j] > 0:
            multi_graph.add_edge(i, j, weight=mst[i][j])
multi_graph.add_edges_from(((u, v) for u, v in min_weight_matching), weight=dist_matrix[u][v])

# Step 5: Find Eulerian tour
eulerian_tour = list(nx.eulerian_circuit(multi_graph, source=0))

# Step 6: Convert to Hamiltonian path
visited = set()
hamiltonian_path = []
for u, v in eulerian_tour:
    if u not in visited:
        hamiltonian_path.append(u)
        visited.add(u)
hamiltonian_path.append(hamiltonian_path[0])  # Complete the circuit

# Calculate travel cost
total_cost = sum(dist_matrix[hamiltonian_path[i]][hamiltonian_path[i + 1]] for i in range(len(hamiltonian_path) - 1))

# Output results
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)