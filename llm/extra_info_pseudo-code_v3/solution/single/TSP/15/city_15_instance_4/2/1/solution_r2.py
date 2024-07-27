import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Define cities coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Create distance matrix
cities_np = np.array(cities)
dist_matrix = distance_matrix(cities_np, cities_np)

# Step 1: Create a graph based on the distance matrix
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Step 2: Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 3: Vertices with odd degree
odd_vertices = [v for v, degree in T.degree() if degree % 2 != 0]

# Step 4: Minimum weight perfect matching for odd degree vertices
subgraph = G.subgraph(odd_vertices)
min_weight_match = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Adding matching to MST to get a multigraph with all degrees even
multigraph = nx.MultiGraph(T)
multigraph.add_edges_from(min_weight_match)

# Step 5: Find Eulerian circuit in the multigraph
eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))

# Step 6: Transform Eulerian circuit to a Hamiltonian circuit (shortcutting)
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Ensure it ends where it starts
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Step 7: Calculate total travel cost
total_distance = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output results
print(f'Tour: {hamiltonian_circuit}')
print(f'Total travel cost: {total_distance:.2f}')