import networkx as nx
from itertools import combinations
import math

# Define cities and their coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 58), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Helper function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create a complete weighted graph
G = nx.Graph()
for u in cities:
    for v in cities:
        if u != v:
            G.add_edge(u, v, weight=euclidean_distance(cities[u], cities[v]))

# Step 1: Find the minimum spanning tree
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in T
O = [v for v in T if T.degree[v] % 2 != 0]

# Step 3: Find the minimum weight perfect matching on the induced subgraph of O
M = nx.Graph()
M.add_nodes_from(O)
for u, v in combinations(O, 2):
    M.add_edge(u, v, weight=euclidean_distance(cities[u], cities[v]))

matching = nx.algorithms.matching.min_weight_matching(M, maxcardinality=True)

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Ensure the tour ends at the starting point
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate the total travel cost of the tour
total_travel_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)