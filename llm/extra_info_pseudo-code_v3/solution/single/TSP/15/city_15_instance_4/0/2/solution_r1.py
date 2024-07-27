import numpy as np
import networkx as nx

# Cities and their coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Complete graph of cities with Euclidean distances
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            dist = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
            G.add_edge(i, j, weight=dist)

# Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with odd degree in the MST
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 == 1]

# Minimum-weight perfect matching in the induced subgraph on odd-degree nodes
odd_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Add matching edges to MST to produce an Eulerian graph
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(min_weight_matching)

# Compute the Eulerian tour
eulerian_tour = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert Eulerian tour to Hamiltonian circuit and compute total cost
visited = set()
hamiltonian_circuit = []
total_distance = 0
prev_city = 0

for u, v in eulerian_tour:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)
        total_distance += G[prev_city][v]['weight']
        prev_city = v

# Complete the tour back to the starting point (depot)
hamiltonian_circuit.append(0)
total_distance += G[prev_city][0]['weight']

# Output the tour and the corresponding travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_distance)