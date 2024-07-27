import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Define the coordinates of each city (including the depot city as city 0)
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Create a distance matrix
locations = np.array(list(cities.values()))
dist_matrix = distance_matrix(locations, locations)

# Create a complete graph from the distance matrix
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Compute the MST T of graph G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree in MST T
odd_degree_nodes = [v for v, degree in T.degree() if degree % 2 == 1]

# Step 3: Find minimum weight perfect matching in the subgraph induced by vertices with odd degree
odd_subgraph = nx.Graph()
odd_subgraph.add_nodes_from(odd_degree_nodes)
for u, v in combinations(odd_degree_nodes, 2):
    odd_subgraph.add_edge(u, v, weight=dist_matrix[u][v])
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Step 4: Add the matching edges to MST
H = nx.MultiGraph(T)
H.add_edges_from(matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if not u in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # Complete the circuit by returning to the depot city

# Calculate the total travel cost
total_travel_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)