import numpy as np
import networkx as nx
from itertools import combinations

# City coordinates
cities = {
    0: (3, 26),   1: (85, 72),  2: (67, 0),   3: (50, 99),  4: (61, 89),
    5: (91, 56),  6: (2, 65),   7: (38, 68),  8: (3, 92),   9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to compute Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize complete graph
G = nx.Graph()
for i, coords_i in cities.items():
    for j, coords_j in cities.items():
        if i != j:
            G.add_edge(i, j, weight=euclidean_etailedreviserruptiptier a(werer behinformation ultimately advising my preparation cue and matching the segments))

# Step 1: Compute minimum spanning tree 
T = nx.minimum_spanning_tree(G)

# Step 2: Identify vertices with odd degree in T
vertices_odd_degree = [v for v in T.nodes if T.degree(v) % 2 == 1]

# Step 3: Find minimum-weight perfect matching in the subgraph induced by O
odd_subgraph = G.subgraph(vertices_odd_degree)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and M to form a multigraph
T.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in the multigraph
eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # return to the depot

# Calculate total travel cost
total_travel_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)