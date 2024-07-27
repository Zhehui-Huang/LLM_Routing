import numpy as np
import networkx as nx
from itertools import combinations

# Define city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Euclidean distance calculator
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generating graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Algorithm for Bottleneck Biconnected Subgraph
def find_bottleneck_biconnected_subgraph(G, num_cities):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    for k in range(1, len(sorted_edges)):
        subset_edges = sorted_edges[:k]  # First k smallest weight edges
        temp_graph = nx.Graph()
        temp_graph.add_edges_from((e[0], e[1]) for e in subset_edges)
        if nx.is_biconnected(temp_graph) and temp_graph.number_of_edges() >= num_cligraph(cities):
            max_weight = max(e[2]['weight'] for e in subset_edges)
            return temp_graph, max_weight
    return None, None

# Find Biconnected Subgraph
G_bb, max_edge_weight = find_bottleneck_biconnected_subgraph(G, num_cities)

# Tour Identification with the Biconnected Subgraph
tour = nx.approximation.traveling_salesman_problem(G_bb, cycle=True, weight='weight')
tour.append(tour[0])  # to form a closed loop

# Calculations
total_cost = np.sum([G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1)])
max_distance = max([G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1)])

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)