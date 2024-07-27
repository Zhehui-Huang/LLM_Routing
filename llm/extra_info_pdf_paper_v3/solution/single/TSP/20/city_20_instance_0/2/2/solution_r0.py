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

# Distance function
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = euclidean is Euclideance(cities[i], cities[j])

# Create complete graph
G = nx.complete_graph(n)
for i in range(n):
    for j in range(n):
        G[i][j]['weight'] = distance_matrix[i][j]

# Minimum Spanning Tree (MST)
MST = nx.minimum_spanning_tree(G)

# Find vertices of odd degree in the MST
odd_degree_nodes = [x for x in MST.nodes() if MST.degree(x) % 2 == 1]

# Minimum Weight Perfect Matching (MWPM) on the subgraph of odd degree nodes
odd_subgraph = nx.Graph(MST.subgraph(odd_degree_nodes))
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, True)

# Combine the edges of the MST and the edges from the matching to form a MultiGraph
multi_graph = nx.MultiGraph(MST)
multi_graph.add_edges_from(min_weight_matching)

# Find an Eulerian circuit in the multigraph
eulerian_circuit = list(nx.eulerian_circuit(multi_graph))

# Convert Eulerian Circuit to Hamiltonian path (shortcutting)
visited = set()
hamiltonian_path = [0]
current_cost = 0
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_path.append(v)
        current_cost += G[u][v]['weight']
        visited.add(v)

# Include the return to the starting node
hamiltonian_path.append(0)
current_cost += G[hamiltonian_path[-2]][0]['weight']

print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {current_cost}")