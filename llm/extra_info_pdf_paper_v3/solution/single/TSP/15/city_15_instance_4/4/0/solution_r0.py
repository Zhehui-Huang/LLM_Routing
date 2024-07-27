import math
import numpy as np
import networkx as nx

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Creating graph with distances
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Constructing the MST using Prim's algorithm
MST = nx.minimum_spanning_tree(G)

# Finding odd degree vertices in the MST
odd_degree_nodes = [node for node, degree in MST.degree() if degree % 2 == 1]

# Creating subgraph with odd degree nodes
odd_subgraph = G.subgraph(odd_degree_nodes)

# Finding minimum cost perfect matching in the odd degree subgraph
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Adding matching edges to MST
multi_graph = nx.MultiGraph(MST)
multi_graph.add_edges_from(matching)

# Finding Eulerian Circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Converting Eulerian Circuit to Hamiltonian Circuit (Shortcutting)
visited = set()
tour = []
for u, v in eulerian_circuit:
    if not u in visited:
        tour.append(u)
        visited.add(u)

# Adding the return to the starting point
tour.append(0)

# Calculate total travel cost of the tour
total_cost = sum(G[u][v]['id_pesos'] for u, v in zip(tour[:-1], tour[1:]))

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")