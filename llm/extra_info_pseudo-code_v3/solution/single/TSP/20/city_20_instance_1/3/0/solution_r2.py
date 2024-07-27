import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx
from networkx.algorithms.matching import max_weight_matching

# Define the coordinates of each city, including the depot
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Function to calculate the Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create the distance matrix
n = len(coordinates)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Step 1: Minimum Spanning Tree (MST)
mst_sparse = minimum_spanning_tree(csr_matrix(dist_matrix))
mst = mst_sparse.toarray()

# Create a graph from MST
G = nx.Graph()
for i in range(n):
    for j in range(n):
        if mst[i][j] > 0:
            G.add_edge(i, j, weight=mst[i][j])

# Step 2: Find vertices with odd degree
odd_degree_vertices = [v for v in G.nodes if G.degree(v) % 2 == 1]

# Step 3: Minimum Weight Perfect Matching on the induced subgraph by odd_degree_vertices
subgraph = G.subgraph(odd_degree_vertices)
min_weight_matching = max_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add matching to the graph
for edge in min_weight_matching:
    G.add_edge(edge[0], edge[1], weight=dist_matrix[edge[0]][edge[1]])

# Step 5: Find Eulerian circuit
euler_circuit = list(nx.eulerian_circuit(G, source=0))

# Step 6: Convert Eulerian to Hamiltonian circuit
hamiltonian_circuit = []
visited = set()
for v, _ in euler_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
hamiltonian_circuit.append(0)  # return to the depot

# Calculate total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)