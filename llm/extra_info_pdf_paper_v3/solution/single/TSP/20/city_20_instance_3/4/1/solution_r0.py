import math
from scipy.spatial import distance
from itertools import combinations
import networkx as nx

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate distances
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Construct a Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree in the MST
odd_degree_vertices = [v for v, degree in mst.degree() if degree % 2 == 1]

# Create the subgraph induced by vertices with odd degree
odd_graph = G.subgraph(odd_degree_vertices)

# Step 3: Find a Minimum-Cost Perfect Matching in the subgraph
# Using the blossom algorithm which handles matchings
perfect_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add matching edges to the MST
mst.add_edges_from(perfect_matching)

# Step 4: Find an Eulerian Circuit in the augmented graph (MST + Matching)
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 5: Make tour Hamiltonian
# Convert Eulerian Circuit to Hamiltonian Circuit:
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # come back to the depot

# Step 6: Calculate the total cost of the tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")