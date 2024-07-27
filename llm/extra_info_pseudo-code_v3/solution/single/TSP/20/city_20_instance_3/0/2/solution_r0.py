import numpy as np
from scipy.spatial.distance import cdist
from networkx import Graph, minimum_spanning_tree, eulerian_circuit, is_eulerian
from networkx.algorithms.matching import min_weight_matching

# Define the cities' coordinates
coordinates = np.array([
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
])

# Compute the pairwise Euclidean distances as the graph weights
distances = cdist(coordinates, coordinates, 'euclidean')

# Create a complete graph with the computed distances
graph = Graph()
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        graph.add_edge(i, j, weight=distances[i][j])

# Step 1: Compute a minimum spanning tree of the graph
mst = minimum_spanning_tree(graph)

# Step 2: Find vertices with odd degree in the MST
odd_vertices = [v for v, d in mst.degree() if d % 2 == 1]

# Step 3: Find a minimum-weight perfect matching among the odd degree vertices
odd_subgraph = graph.subgraph(odd_vertices)
matching = min_weight_matching(odd_subgraph, True, weight='weight')

# Add the matching edges to the MST
mst.add_edges_from(matching)

# Step 4: Form a multigraph (already complete)
# Step 5: Find an Eulerian circuit in the multigraph
assert is_eulerian(mst)
euler_circuit = list(eulerian_circuit(mst))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit (skip repeated vertices)
visited = set()
hamiltonian_circuit = [0]
for u, v in euler_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)

# Compute the total travel cost of the tour
total_cost = sum(distances[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")