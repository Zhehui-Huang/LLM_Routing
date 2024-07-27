import numpy as np
import networkx as nx

# Coordinates of the cities
coordinates = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61),
    (22, 21), (97, 70), (20, 99), (66, 62)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a fully connected graph
G = nx.Graph()
num_cities = len(coordinates)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=euclidean_distance(coordinates[i], coordinates[j]))

# Find the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find all vertices of odd degree in the MST
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 != 0]

# Create a subgraph of G containing only the odd degree vertices
subgraph = G.subgraph(odd]degree_nodes)

# Find a minimum weight perfect matching in the subgraph of odd degree nodes
odd_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add the matching edges to the MST
mst.add_edges_from(odd_matching)

# Create an Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(mst))

# Convert the Eulerian circuit to a Hamiltonian circuit by skipping repeated nodes
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Add the start node to complete the circuit
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the total cost of the Hamiltonian circuit
total_travel_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)