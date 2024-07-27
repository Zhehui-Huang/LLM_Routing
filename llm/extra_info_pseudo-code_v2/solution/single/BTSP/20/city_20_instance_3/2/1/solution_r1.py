import math
import networkx as nx
from networkx.algorithms.connectivity import is_k_edge_connected

def euclidean_distance(coords1, coords2):
    return math.sqrt((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2)

def create_complete_graph(cities):
    G = nx.Graph()
    for i in cities.keys():
        for j in cities.keys():
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def find_biconnected_subgraph(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = []
    for edge in sorted_edges:
        E_BB.append(edge)
        subgraph = nx.Graph()
        subgraph.add_edges_from(E_BB)
        if is_k_edge_connected(subgraph, 2):
            return subgraph

    return subgraph  # In case no sufficient biconnectivity is found with fewer edges.

def find_tour_and_max_distance(graph):
    # Since finding an exact Hamiltonian circuit is NP-hard, use approximate TSP approach.
    cycle = list(nx.approximation.traveling_salesman_problem(graph, cycle=True))
    total_cost = sum(graph[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle) - 1)) + graph[cycle[-1]][cycle[0]]['weight']
    max_distance = max(graph[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle) - 1))
    return cycle + [cycle[0]], total_cost, max_distance

cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

G = create_complete_graph(cities)
subgraph = find_biconnected_subgraph(G)
tour, total_cost, max_distance = find_tour_and_max_distance(subgraph)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)