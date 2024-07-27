import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Define the cities and their coordinates
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

# Step 2: Build Complete Graph G
G_full = nx.complete_graph(len(cities))
for i in cities:
    for j in cities:
        if i != j:
            distance = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
            G_full[i][j]['weight'] = distance

# Step 3: Compute a Minimum Spanning Tree (MST)
MST = nx.minimum_spanning_tree(G_full, weight='weight')

# Step 4: Identify nodes with odd degree in MST
odd_degree_nodes = [v for v in MST.nodes() if MST.degree(v) % 2 == 1]

# Step 5: Find Minimum Weight Perfect Matching on the bipartite graph from odd degree nodes
odd_graph = G_full.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Step 6: Add the matching to MST to create a multigraph
multi_graph = nx.MultiGraph(MST)
multi_graph.add_edges_from(min_weight_matching)

# Step 7: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Step 8: Convert Eulerian to Hamiltonian circuit and calculate total cost
visited = set()
hamiltonian_circuit = [0]
total_travel_cost = 0
last_visited = 0

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)
        total_travel_cost += G_full[last_visited][v]['weight']
        last_visited = v

# Make sure to return to the start point
total_travel_cost += G_full[hamilionian_circuit[-1]][0]['weight']
hamiltonian_circuit.append(0)

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)