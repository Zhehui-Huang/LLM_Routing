import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix
import networkx as nx
from itertools import combinations

# Coordinates of the cities including the depot
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create a fully connected graph with distances as weights
size = len(cities)
dist_matrix = np.zeros((size, size))
for i in range(size):
    for j in range(size):
        if i != j:
            dist_matrix[i][j] = distance(i, j)
        else:
            dist_matrix[i][j] = float('inf')

# Step 1: Compute a minimum spanning tree T of G
mst_matrix = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()

# Convert the MST matrix to a networkx graph
T = nx.Graph()
for i in range(size):
    for j in range(size):
        if mst_matrix[i][j] > 0:
            T.add_edge(i, j, weight=mst_matrix[i][j])

# Step 2: Identify the set O of vertices with odd degree in T
odd_degree_nodes = [i for i in range(size) if T.degree(i) % 2 == 1]

# Step 3: Find minimum-weight perfect matching
min_weight_matching = nx.algorithms.matching.min_weight_matching(nx.complete_graph(odd_degree_nodes, create_using=nx.Graph()), weight=lambda u, v: distance(u,v))

# Step 4: Combine edges of T and M to form a multi-graph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]  # start at the depot city 0
for x, y in eulerian_circuit:
    if x not in visited:
        visited.add(x)
        hamiltonian_circuit.append(x)
    if y not in visited:
        visited.add(y)
        hamiltonian_circuit.append(y)
hamiltonian_circuit.append(0)  # return to the depot city

# Calculate total travel cost
total_cost = sum(distance(hamiltonian_circuit[i], hamiltonian_circuit[i + 1]) for i in range(len(hamiltonian_circuit) - 1))

# Output results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")