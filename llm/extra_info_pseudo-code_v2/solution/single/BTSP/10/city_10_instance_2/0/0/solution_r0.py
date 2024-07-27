import math
from itertools import combinations, permutations
import networkx as nx

# City coordinates: id and (x, y)
coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Generate the complete graph
def create_complete_graph(node_coords):
    G = nx.Graph()
    for pair in combinations(node_coords.keys(), 2):
        c1, c2 = node_coords[pair[0]], node_coords[pair[1]]
        dist = euclidean_distance(c1, c2)
        G.add_edge(pair[0], pair[1], weight=dist)
    return G

G = create_complete_graph(coordinates)

# Algorithm BB: Find bottleneck-optimal biconnected subgraph
def algorithm_bb(graph):
    edges_sorted = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = nx.Graph()
    E_BB.add_nodes_from(graph.nodes())
    for u, v, data in edges_sorted:
        E_BB.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(E_BB):
            break
    return E_BB

G_bb = algorithm_bb(G)

def find_hamiltonian_path(graph):
    def is_valid_path(G, path):
        for i in range(len(path) - 1):
            if (path[i], path[i+1]) not in G.edges():
                return False
        return True

    cities = list(graph.nodes())
    for perm in permutations(cities):
        if perm[0] == 0 and is_valid_path(graph, perm + (0,)):  # ensure it starts/ends at depot (node 0)
            return perm + (0,)
    return None

# Find the approximate optimal Hamiltonian path in G^2
def find_approx_tour_in_G2(graph):
    G2 = nx.Graph()
    for u in graph.nodes():
        for v in graph.nodes():
            if u != v and nx.has_path(graph, u, v):
                shortest_path_length = nx.shortest_path_length(graph, source=u, target=v, weight='weight')
                G2.add_edge(u, v, weight=shortest_path_length)
    return find_hamiltonian_path(G2)

tour = find_approx_tour_in_G2(G_bb)

# Calculate total and maximum travel cost
def tour_cost_details(tour, graph):
    total_cost = sum(graph[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))
    max_cost = max(graph[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))
    return total_cost, max_tp

total_cost, max_cap = tour_cost_details(tour, G_bb)

# Output results
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_cap}")