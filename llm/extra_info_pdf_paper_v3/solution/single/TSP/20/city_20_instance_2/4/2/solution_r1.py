import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np
import networkx as nx

# Locations of cities (Index 0 is depot)
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Creating MST using the distance matrix
mst = minimum_spanning_tree(csr_matrix(distance_matrix))

# Find vertices with odd degree in the MST
G = nx.from_scipy_sparse_matrix(mst)
odd_degree_nodes = [v for v, d in G.degree() if d % 2 == 1]

# Find minimum weight perfect matching for odd degree vertices
min_weight_matching = nx.algorithms.matching.min_weight_matching(G.subgraph(odd_degree_nodes), maxcardinality=True)

# Add edges from the minimum weight matching to the graph
for edge in min_weight_matching:
    G.add_edge(*edge)

# Find Eulerian circuit (This is possible as all vertex degrees are even now)
eulerian_circuit = list(nx.eulerian_circuit(G, source=0))

# Convert the Eulerian circuit to a Hamiltonian circuit (path visiting each node once)
hamiltonian_path = [0]
visited = set([0])
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_path.append(v)
        visited.add(v)

hamiltonian_path.append(0)  # return to the depot

# Calculate the total cost of the Hamiltonian path
total_cost = sum(distance_matrix[hamiltonian_path[i]][hamiltonian_path[i + 1]] for i in range(len(hamiltonian_path) - 1))

print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)