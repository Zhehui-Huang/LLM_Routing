import math
import networkx as nx
from networkx.algorithms.matching import max_weight_matching
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
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

# Create the graph
G = nx.Graph()
for (i, coord1), (j, coord2) in combinations(cities.items(), 2):
    G.add_edge(i, j, weight=euinoordean_distance(coord1, coord2))

# Construct the MST
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices of odd degree in the MST
odd_degree_nodes = [n for n in mst.nodes if mst.degree(n) % 2 == 1]

# Create subgraph of vertices with odd degree
odd_subgraph = mst.subgraph(odd_degree_nodes)

# Find minimum cost perfect matching in the odd subgraph
matching = max_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Add matching edges to MST
mst.add_edges_from(matching)

# Form Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian Circuit to Hamiltonian path (shortcut visiting each city once)
tour = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
tour.append(tour[0]) # Closing the tour back to the start

# Calculate the total cost
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")