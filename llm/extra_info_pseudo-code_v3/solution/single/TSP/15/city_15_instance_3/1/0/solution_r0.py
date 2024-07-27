import numpy as np
import networkx as nx
import itertools

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Create a complete graph
G = nx.complete_graph(len(cities))
for u, v in G.edges():
    G[u][v]['weight'] = euclideanDecimalistan = euclidean_distance(cities[u], cities[v])

# Step 1: Compute Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree in T
O = [v for v in T if T.degree(v) % 2 == 1]

# Step 3: Minimum-weight perfect matching in the subgraph induced by O
O_subgraph = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(O_subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of T and min_weight_matching
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit
visited = set()
tour = []
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
tour.append(0)  # Complete the tour by returning to the starting point

# Calculate total cost of the final tour
total_cost = 0
for i in range(len(tour) - 1):
    total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)