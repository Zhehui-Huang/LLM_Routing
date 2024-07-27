import numpy as np
import networkx as nx

# Coordinates of the cities including the depot
coordinates = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Function to compute the Euclidean distance matrix
def calculate_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist = np.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
            dist_matrix[i, j] = dist_matrix[j, i] = dist
    return dist_matrix

# Calculate the distance matrix
dist_matrix = calculate_distance_matrix(coordinates)

# Create graph G from distance matrix
G = nx.Graph()
n = len(dist_matrix)
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# 1. Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# 2. Identify vertices with an odd degree in MST
odd_degree_nodes = [node for node in mst.nodes() if mst.degree(node) % 2 == 1]

# 3. Create subgraph of odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)

# 4. Find minimum-weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# 5. Add matching edges to MST
mst.add_edges_from(matching)

# 6. Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))
circuit = []
visited = set()

# Convert to Hamiltonian circuit by skipping repeated nodes
for u, v in eulerian_circuit:
    if v not in visited or v == 0:  # Allow return to starting point
        circuit.append(v)
        visited.add(v)

# Ensure the tour starts and ends at the depot, circuit[0] is 0 by design but reaffirm for clarity and to close loop
circuit.append(0)

# Calculate the total travel cost
total_travel_cost = sum(dist_matrix[circuit[i]][circuit[i+1]] for i in range(len(circuit)-1))

print(f"Tour: {circuit}")
print(f"Total travel cost: {total_travel_cost:.2f}")