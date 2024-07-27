import math
import networkx as nx

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
    14: (6, 99)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:  # avoid self-loops
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Function for building a bottleneck-optimal biconnected subgraph
def build_biconnected_subgraph(N, G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    h = nx.Graph()
    h.add_nodes_from(N)
    for edge in sorted_edges:
        h.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(h):
            return h
    return h

# Building the subgraph from the complete graph
h_graph = build_biconnected_subgraph(G.nodes, G)

# Hamiltonian circuit from the biconnected subgraph
tour = list(nx.approximation.traveling_salesman_problem(h_graph, weight='weight', cycle=True))

# Calculate total travel cost and maximal distance between consecutive cities in the tour
total_cost = sum(h_graph[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))
max_distance = max(h_graph[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Format the output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")