import math
import networkx as nx
from scipy.spatial import distance_matrix

# Coordinates of the cities
city_coords = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Get the number of cities
num_cities = len(city_coords)

# Distance matrix
dist_matrix = distance_matrix(city_coords, city_coords)

# Create a complete graph
G = nx.complete_graph(num_cities)

# Update graph with distances
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.edges[i, j]['weight'] = dist_matrix[i][j]

# Find Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with odd degree in MST
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Minimum Weight Perfect Matching (MCPM) in the subgraph of odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add matching edges to MST
mst.add_edges_from(min_pc_matching)

# Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Making the tour a Hamiltonian cycle
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Ensuring we return to the start position
hamiltonian_circuit.append(0)

# Calculate the total cost of this tour
total_cost = 0
for i in range(1, len(hamiltonian_circuit)):
    total_cost += dist_matrix[hamiltonian_circuit[i-1]][hamiltonian_circuit[i]]

# Printing results as per format
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")