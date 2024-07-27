import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from networkx import Graph, eulerian_circuit
from networkx.algorithms.matching import min_weight_matching

# Define cities and their positions
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create the complete graph with weights
num_cities = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Step 1: Compute the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(csr_matrix(distance_matrix)).toarray()

# Step 2: Identify vertices with odd degree in the MST
degree = np.sum(mst != 0, axis=0)
odd_degree_vertices = [i for i in range(num_cities) if degree[i] % 2 == 1]

# Step 3: Find minimum-weight perfect matching M on odd degree vertices
subgraph = csr_matrix([[distance_matrix[i][j] if i in odd_degree_vertices and j in odd_degree_vertices else 0
                        for j in range(num_cities)] for i in range(num_cities)])
matching = min_weight_matching(Graph(subgraph), maxcardinality=True, weight='weight')

# Step 4: Add edges from matching to the MST to form multi-graph H
multi_graph = mst.copy()
for edge in matching:
    # As matching gives us an unordered pair, we add both edge directions
    multi_graph[edge[0]][edge[1]] = distance_matrix[edge[0]][edge[1]]
    multi_graph[edge[1]][edge[0]] = distance_matrix[edge[1]][edge[0]]

# Step 5: Find an Eulerian circuit in the multi-graph
euler_graph = Graph(multi_graph)
circuit = list(eulerian_circuit(euler_graph, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # return to the start

# Calculate total travel cost
total_cost = sum(distance_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)