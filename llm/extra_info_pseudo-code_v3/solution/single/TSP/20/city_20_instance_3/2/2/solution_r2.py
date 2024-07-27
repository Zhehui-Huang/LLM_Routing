import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84), 
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i, j] = euclidean(cities[i], cities[j])
    return dist_matrix

dist_matrix = calculate_distance_matrix(list(cities.values()))

# Create graph from distance matrix
G = nx.Graph()
n = len(cities)
for i in range(n):
    for j in range(i+1, n):
        G.add_edge(i, j, weight=dist_matrix[i, j])

# Step 1: Compute MST T of G
mst_tree = nx.minimum_spanning_tree(G)

# Step 2: Get all nodes with an odd degree in MST
odds = [x for x in mst_tree.nodes() if mst_tree.degree(x) % 2 == 1]

# Step 3: Minimum-weight perfect matching on the nodes with odd degree
odd_subgraph = mst_tree.subgraph(odds)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Build the multigraph that incorporates edges from the MST and from the minimum-weight matching
multi_graph = mst_tree.copy()
multi_graph.add_edges_from(min_weight_matching)

# Step 5: Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Construct a Hamiltonian circuit by skipping visited nodes
visited = set()
path = []
for u, v in eulerian_circuit:
    if u not in visited:
        path.append(u)
        visited.add(u)
path.append(0)  # back to the starting node

# Calculate total cost
total_cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))

print("Tour:", path)
print("Total travel cost:", total_cost)