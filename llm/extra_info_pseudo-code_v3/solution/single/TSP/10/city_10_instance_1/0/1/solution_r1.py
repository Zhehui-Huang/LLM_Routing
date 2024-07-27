import math
import numpy as np
import networkx as nx

# Define cities and their positions
cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create the graph
num_cities = len(cities)
G = nx.Graph()
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Compute a Minimum Spanning Tree (MST) of G
mst = nx.minimum_spanning_tree(G)

# Step 2: Identify the set O of vertices with an odd degree in T
odd_degree_vertices = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

# Create a subgraph induced by odd degree vertices
odd_subgraph = G.subgraph(odd_degree_vertices)

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(mst)
H.add_edges_from(matching)

# Step 5: Find an Eulerian circuit in H
euler_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
for u, v in euler_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
hamiltonian_circuit.append(0)  # complete the cycle to return to the depot

# Calculate total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)