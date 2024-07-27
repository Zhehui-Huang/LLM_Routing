import numpy as np
import networkx as nx

# Define city positions
city_positions = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate Euclidean distances between all pairs of cities
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

num_cities = len(city_positions)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        distance_matrix[i][j] = distance_matrix[j][i] = euclidean_distance(city_positions[i], city_positions[j])

# Construct the graph and compute the Minimum Spanning Tree (MST)
G = nx.Graph()
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=distance_matrix[i][j])
MST = nx.minimum_spanning_tree(G)

# Find vertices with odd degree in the MST
odd_degree_vertices = [v for v in MST.nodes if MST.degree[v] % 2 != 0]

# Create subgraph limited to the odd_degree_vertices and find perfect min weight matching
subgraph = G.subgraph(odd_degree_vertices)
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add the matching edges to the MST
MST.add_edges_from(matching)

# Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))

# Convert Eulerian circuit to a Hamiltonian circuit by skipping visited nodes
visited = set()
tour = []
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
tour.append(tour[0])  # to return to the depot

# Calculate the total travel cost of the tour
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Display results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")