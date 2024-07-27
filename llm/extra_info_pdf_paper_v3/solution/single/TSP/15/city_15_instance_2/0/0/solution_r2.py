import math
import networkx as nx
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of cities
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

# Build the graph
G = nx.Graph()
for (i, coord1), (j, coord2) in combinations(cities.items(), 2):
    G.add_edge(i, j, weight=euclidean_idistance(coord1, coord2))

# Create MST
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with odd degree in the MST
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

# Create the subgraph induced by nodes with odd degree
odd_subgraph = mst.subgraph(odd_degree_nodes)

# Find a perfect minimum-cost matching in the odd degree subgraph
matching = nx.algorithms.matching.max_weight_matching(odd_subgraph, maxcardinality=True)

# Create Eulerian Circuit: add matching edges to MST
mst.add_edges_from(matching)

# Find an Eulerian circuit from mst graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian Circuit to Hamiltonian Circuit by skipping repeated nodes
visited = set()
tour = []
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
tour.append(0)  # return to the start city (depot)

# Calculate the total travel cost
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")