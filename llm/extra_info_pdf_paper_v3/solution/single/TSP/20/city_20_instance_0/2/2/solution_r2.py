import numpy as np
import networkx as nx

# Define cities
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate the distance matrix
n = len(cities)
G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(cities[i], cities[j])
        G.add_edge(i, j, weight=dist)

# Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find nodes with odd degree in the MST
odd_degree_nodes = [u for u in mst.nodes() if mst.degree(u) % 2 == 1]

# Subgraph of G induced by nodes with odd degree
odd_graph = G.subgraph(odd_degree_nodes)
# Find Minimum Cost Perfect Matching in the induced subgraph
matches = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')
# Add matching edges to the MST
mst.add_edges_from(matches)

# Get an Eulerian circuit from the multi-graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Construct a Hamiltonian cycle by visiting nodes as per the Eulerian circuit but skipping already visited nodes
hamiltonian_cycle = [0]
visited = set(hamiltonian_cycle)
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_cycle.append(v)
        visited.add(v)
hamiltonian_cycle.append(0)  # Return to the depot city

# Calculate the total travel cost
total_cost = sum(G[hamiltonian_cycle[i]][hamiltonian_cycle[i+1]]['weight'] for i in range(len(hamiltonian_cycle)-1))

# Output the result
print(f"Tour: {hamiltonian_cycle}")
print(f"Total travel cost: {total_cost}")