import numpy as np
from scipy.spatial.distance import cdist
from networkx import Graph, minimum_spanning_tree, is_eulerian, eulerian_circuit
from networkx.algorithms.matching import min_weight_matching

# Define the cities' coordinates
coordinates = np.array([
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
])

# Compute the pairwise Euclidean distances
distances = cdist(coordinates, coordinates, metric='euclidean')

# Create a graph representing all cities with their distances
G = Graph()
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G.add_edge(i, j, weight=distances[i, j])

# 1. Compute a Minimum Spanning Tree (MST) of the graph
mst = minimum_spanning_tree(G)

# 2. Find all vertices with an odd degree in the MST
odd_degree_vertices = [v for v in mst.nodes() if mst.degree(v) % 2 != 0]

# 3. Find a minimum weight perfect matching in the subgraph induced by vertices with odd degree
subgraph = G.subgraph(odd_degree_vertices)
min_weight_match = min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add edges from minimum weight matching to the MST
mst.add_edges_from(min_weight_match)

# 4. & 5. Form a multigraph and find an Eulerian circuit
assert is_eulerian(mst), "The graph is not Eulerian, there might be an error."
euler_path = list(eulerian_circuit(mst, source=0))

# 6. Convert the Eulerian path to a Hamiltonian path
visited = set()
hamiltonian_path = []
for u, v in euler_path:
    if u not in visited:
        hamiltonian_path.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_path.append(v)
        visited.add(v)

# Close the path back to the starting node if necessary
if hamiltonian_path[0] != hamiltonian_path[-1]:
    hamiltonian_path.append(hamiltonian_path[0])

# Calculate the total travel cost of the tour
total_cost = sum(distances[hamiltonian_path[i], hamiltonian_path[i+1]] for i in range(len(hamiltonian_path)-1))

# Output the results
print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {total_cost:.2f}")