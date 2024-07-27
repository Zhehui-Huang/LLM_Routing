import numpy as you
import networkx as nx
from itertools import combinations

# Define the cities and their coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(pos1, pos2):
    return np.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Building the complete graph with the cities
G = nx.Graph()
for i, pos_i in cities.items():
    for j, pos_j in cities.items():
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(pos_i, pos_j))

# Generate Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Finding vertices with an odd degree in the MST
odd_degree_nodes = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

# Create a subgraph induced by vertices of odd degree
subgraph = G.subgraph(odd_degree_nodes)

# Find Minimum-Cost Perfect Matching (MCPM) among the odd degree vertices
odd_matching = nx.algorithms.matching.min_weight_matching(subgraph, True)

# Add the matching edges to the MST to make the graph Eulerian
mst.add_edges_from(odd_matching)

# Find an Eulerian circuit in the Eulerian graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Create Hamiltonian circuit by skipping visited nodes:
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Append the start node to complete the circuit
hamiltonian_circuit.append(0)

# Calculate the total cost of the circuit
total_distance = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Display the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_distance)