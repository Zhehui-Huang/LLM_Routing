import networkx as nx
from itertools import combinations
import math

# Define cities and their coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
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

# Step 1: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G)

# Step 2: Identify the set O of vertices with odd degree in T
O = [v for v in T if T.degree[v] % 2 != 0]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
subgraph = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Step 4: Combine edges of T and min_weight_matching to form multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Ensure the robot returns to the depot city
hamiltonian_circuit.append(0)

# Calculate the total travel cost
total_travel_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Display output as per formatting requirements
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_travel_cost:.2f}")