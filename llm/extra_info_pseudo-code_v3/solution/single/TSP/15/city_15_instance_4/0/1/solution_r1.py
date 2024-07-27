import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree

# Define the cities' coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate the distance matrix
positions = np.array(list(cities.values()))
dist_matrix = squareform(pdist(positions, 'euclidean'))

# Number of cities
n = len(cities)

# Step 1: Finding Minimum Spanning Tree (MST)
graph = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        graph.add_edge(i, j, weight=dist_matrix[i][j])

mst_tree = nx.minimum_spanning_tree(graph, weight='weight')

# Step 2: Finding vertices with odd degree
odd_vertexes = [v for v, d in mst_tree.degree() if d % 2 == 1]

# Step 3: Minimum weight perfect matching (Using NetworkX's max_weight_matching)
odd_vertex_subgraph = mst_tree.subgraph(odd_vertexes)
perfect_matching = nx.algorithms.max_weight_matching(odd_vertex_subgraph, True)

# Step 4: Combine the edges of MST and perfect matching to create a multigraph
multigraph = nx.MultiGraph(mst_tree)
multigraph.add_edges_from(perfect_matching)

# Step 5: Find the Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multigraph))

# Step 6: Convert Eulerian circuit to Hamiltonian path (shortcutting)
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Add return to the starting point
hamiltonian_circuit.append(0)

# Calculate the total cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_catalog[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output tour and total travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)