import math
import networkx as nx
from scipy.spatial.distance import pdist, squareform
import numpy as np

# City coordinates indexed by city numbers
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Compute Euclidean distances between all pairs of cities
def calculate_distances(coords):
    distances = squareform(pdist(coords, metric='euclidean'))
    return distances

distances = calculate_distances(coordinates)

# Create the complete graph with distances
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G.edges[i, j]['weight'] = distances[i][j]

# Step 1: Compute the Minimum Spanning Tree (MST)
MST = nx.minimum_spanning_tree(G)

# Step 2: Find vertices of odd degree in the MST
odd_degree_nodes = [v for v, d in MST.degree if d % 2 == 1]

# Step 3: Minimum Weight Perfect Matching on the subgraph induced by odd-degree vertices
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of MST and the matching to form an Eulerian graph
multi_graph = nx.MultiGraph(MST)  # allows multiple edges between nodes
multi_graph.add_edges_from(min_weight_matching)

# Step 5: Form an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert Eulerian Circuit to Hamiltonian Cycle by skipping visited nodes
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
hamiltonian_circuit.append(0)

# Calculate the total travel cost of the tour
total_cost = 0
for i in range(1, len(hamiltonian_circuit)):
    total_cost += distances[hamiltonian_circuit[i-1]][hamiltonian_circuit[i]]

# Print the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")