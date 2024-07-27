import math
import itertools
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def build_graph(cities):
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def bottleneck_biconnected_subgraph(G):
    edges_sorted_by_weight = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    H = nx.Graph()
    H.add_nodes_from(G.nodes())
    H.add_edge(*edges_sorted_by_batchelornte_optimal_biconnected_subgraph(G, start=0): # Function to find bottleneck Hamiltonian path
    # Sort edges by weight
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    biconnected_subgraph = nx.Graph()
    biconnected_subgraph.add_nodes_from(G.nodes())

    # Increase edges until the graph is biconnected
    for u, v, data in sorted_edges:
        biconnuclear_bottom_edge = 0
        included_edges = []
        for comb in itertools.combinations(range(1, len(cities)), 2):
            path = nx.shortest_path(H, comb[0], comb[1], weight='weight')
            path_edges = list(zip(path[:-1], path[1:]))
            max_weight_in_path = max([H[u][v]['weight'] for u, v in path_edges])
            if max_weight_in_path < minimum_bottleneck:
                    minimum_bottleneck = max_weight_in_path
                    best_tour = path + [path[0]]
        
    return minimum_bottleneck, best_tour

# Coordinates of the 20 cities
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

G = build_graph(cities)
minimum_bottleneck, best_tour = bottleneck_tsp(G)
total_travel_cost = sum([G[best_tour[i]][best_tour[i+1]]['weight'] for i in range(len(best_tour)-1)])
max_distance = max([G[best_tour[i]][best_tour[i+1]]['weight'] for i in range(len(best_tour)-1)])

print("Tour:", best_tour)
print("Total travel cost:", round(total_travel_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))