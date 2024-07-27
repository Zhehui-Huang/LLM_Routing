import math
import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix
from itertools import combinations

# Step 1: Define the cities and their coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Step 2: Calculate distances
coords = np.array(list(cities.values()))
dist_matrix = distance_matrix(coords, coords)

# Step 3: Create graph G
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Step 4: Compute a minimum spanning tree T
T = nx.minimum_spanning_tree(G)

# Step 5: Find vertices with odd degree in T
odd_degree_nodes = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 6: Compute minimum weight perfect matching on vertices with odd degree
odd_degree_subgraph = G.subgraph(odd_degree_nodes)
matching = nx.algorithms.matching.min_weight_matching(odd_degree_subgraph, maxcardinality=True)

# Step 7: Combine edges of T and matching M to form multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(matching)

# Step 8: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 9: Create a function to convert Eulerian circuit to Hamiltonian circuit
def create_hamiltonian_circuit(circuit):
    path = []
    visited = set()
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # append the start city to make it a cycle
    return path

# Step 10: Convert Eulerian circuit to Hamiltonian circuit
hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit)

# Step 11: Calculate travel cost of the tour
def calculate_total_cost(path, dist_matrix):
    total_cost = sum(dist_matrix[path[i], path[i+1]] for i in range(len(path) - 1))
    return total_cost

# Step 12: Calculate total travel cost
total_travel_cost = calculate_total_cost(hamiltonian_circuit, dist_matrix)

# Format output to ensure no decimal precision issues
total_travel_cost = round(total_travel_cost, 1)

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)