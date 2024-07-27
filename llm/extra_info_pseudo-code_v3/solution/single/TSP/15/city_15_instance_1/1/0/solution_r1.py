import math
import networkx as nx
from itertools import combinations

# Coordinates of cities including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create a complete graph with the cities as nodes and set edge weights as distances
n = len(coordinates)
G = nx.complete_graph(n)
for i in range(n):
    for j in range(i+1, n):
        dist = euclidean_distance(coordinates[i], coordinates[j])
        G[i][j]['weight'] = dist

# Step 1: Compute a minimum spanning tree (MST) of G
T = nx.minimum_spanning_tree(G, algorithm='kruskal')

# Step 2: Find vertices of odd degree in the MST
odd_degree_nodes = [v for v in T.nodes if T.degree(v) % 2 == 1]

# Step 3: Find a minimum weight perfect matching among the odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Step 4: Combine edges of T and the matching to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H (it will exist because all vertex degrees are even)
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit (shortcutting repeated nodes)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # complete the circuit by returning to the start

# Calculate the total travel cost
total_travel_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)