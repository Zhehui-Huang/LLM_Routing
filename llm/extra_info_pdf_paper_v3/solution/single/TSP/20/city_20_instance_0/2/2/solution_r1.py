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

# Distance function using Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph of cities with distances as weights
n = len(cities)
G = nx.complete_graph(n)
for i in range(n):
    for j in range(i + 1, n):
        G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])

# Compute Minimum Spanning Tree (MST)
MST = nx.minimum_spanning_tree(G)

# Find vertices with odd degrees in MST
odd_degree_nodes = {x for x in MST.nodes() if MST.degree(x) % 2 == 1}

# Induced subgraph of odd degree vertices
odd_subgraph = G.subgraph(odd_degree_nodes)

# Minimum Weight Perfect Matching (MWPM)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Combine MST and matching to get a multigraph
multi_graph = nx.MultiGraph(MST)
multi_unmatched_edges = {e for e in min_weight_matching if not multi_graph.has_edge(*e)}
multi_graph.add_edges_from(multi_unmatched_edges)

# Get an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Create the Hamiltonian circuit (shortcutting visited nodes)
hamiltonian_circuit = [0]  # start at the depot
visited = set(hamiltonian_circuit)
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # return to the starting city, depot

# Calculate the total travel cost of the Hamiltonian circuit
total_travel_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_travel_cost:.2f}")