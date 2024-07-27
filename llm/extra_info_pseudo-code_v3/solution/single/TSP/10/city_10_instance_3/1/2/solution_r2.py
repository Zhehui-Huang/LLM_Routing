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
        G[i][j]['weight'] = dist_matrix[i, j]
        G[j][i]['weight'] = dist_matrix[j, i]

# Step 1: Compute the MST T of graph G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree in MST T
odd_degree_nodes = [v for v, degree in T.degree() if degree % 2 == 1]

# Step 3: Make a complete graph on the odd degree nodes and find the optimal matching
odd_subgraph = nx.complete_graph(odd_degree_nodes)
for i in odd_degree_nodes:
    for j in odd_degree_nodes:
        if i != j:
            odd_subgraph.add_edge(i, j, weight=dist_matrix[i][j])

matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of the MST and matching to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert eulerian to a simple path
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0) # to ensure return to the depot city

# Calculate the total trip cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)