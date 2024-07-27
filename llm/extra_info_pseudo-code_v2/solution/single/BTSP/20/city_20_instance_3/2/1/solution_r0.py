import math
import networkx as nx
from itertools import combinations

# Coordinates of each city
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(p1, p2):
    """Calculates the Euclidean distance between two points."""
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def create_graph(cities):
    """Creates a complete graph from the cities dictionary"""
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def find_bottleneck_biconnected_subgraph(G):
    """Applies Algorithm BB to find the bottleneck-optimal biconnected subgraph of G."""
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    subsets = []  # to store subsets and check biconnectivity
    for edge in edges_sorted:
        subsets.append(edge)
        H = nx.Graph()
        H.add_edges_from(subsets)
        if nx.is_biconnerected(H):
            return H
    return None

def find_bottleneck_tour(G, subgraph):
    """Identifies an appropriate Hamiltonian cycle (approximation) in the squared biconnected subgraph."""
    G2 = nx.Graph()
    for u in subgraph.nodes():
        for v in subgraph.nodes():
            if u != v:
                if nx.has_path(subgraph, u, v):
                    all_paths = list(nx.all_simple_paths(subgraph, source=u, target=v))
                    min_path_length = min(len(p) for p in all_paths)
                    if min_path_length == 2:
                        G2.add_edge(u, v, weight=max(G[u][p[1]]['weight'], G[v][p[1]]['weight']) for p in all_paths if len(p)==3)

    cycle = list(nx.approximation.traveling_salesman_problem(G2, cycle=True))
    return cycle

def tour_cost_and_bottleneck(G, tour):
    total_cost = sum(G[tour[i]][tour[i-1]]['weight'] for i in range(1, len(tour)))
    max_distance = max(G[tour[i]][tour[i-1]]['weight'] for i in range(1, len(tour)))
    return total_cost, max_distance

# Generate the graph
G = create_graph(cities)
subgraph = find_bottleneck_biconnected_subgraph(G)
tour = find_bottleneck_tour(G, subgraph)
total_cost, max_distance = tour_cost_and_bottleneck(G, tour)

# Returning the results
tour.append(tour[0])  # To complete the cycle
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)