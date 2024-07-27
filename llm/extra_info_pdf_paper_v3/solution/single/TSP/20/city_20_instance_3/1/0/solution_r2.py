import math
from itertools import combinations
import networkx as nx
from scipy.spatial import distance_matrix

def compute_euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Coordinates of the cities
cities_coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Create full graph
n = len(cities_coordinates)
G = nx.Graph()

# Adding nodes and edges with weights based on Euclidean distance
for i in range(n):
    for j in range(i + 1, n):
        distance = compute_euclidean_distance(cities_coordinates[i], cities_coordinates[j])
        G.add_edge(i, j, weight=distance)

# Minimum Spanning Tree (MST) of the graph
mst = nx.minimum_spanning_tree(G)

# Nodes with odd degree in MST
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 == 1]
odd_degree_subgraph = G.subgraph(odd_degree_nodes)

# Minimum Weight Perfect Matching on the odd degree subgraph
matches = nx.algorithms.matching.min_weight_matching(odd_degree_subgraph, maxcardinality=True, weight='weight')

# Combine the MST and the matching to make the graph Eulerian
mst.add_edges_from(matches)

# Getting an Eulerian circuit from the graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Shortcutting the Eulerian circuit into a Hamiltonian circuit (TSP tour)
visited = set()
Hamiltonian_path = [0]  # Starting at the depot
for u, v in eulerian_circuit:
    if v not in visited:
        Hamiltonian_path.append(v)
        visited.add(v)
Hamiltonian_path.append(0)  # Return to depot

# Total travel cost calculation
total_travel_cost = sum(G[u][v]['weight'] for u, v in zip(Hamiltonian_path[:-1], Hamiltonian_path[1:]))

# Output the results
print("Tour:", Hamiltonian_path)
print("Total travel cost:", total_travel_cost)