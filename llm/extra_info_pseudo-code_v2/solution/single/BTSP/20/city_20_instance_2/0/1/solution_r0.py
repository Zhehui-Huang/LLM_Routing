import networkx as nx
import math
from itertools import permutations

# Given city coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 91),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create a complete graph
def create_graph():
    G = nx.complete_graph(len(cities))
    for u, v, data in G.edges(data=True):
        data['weight'] = distance(u, v)
    return G

# Algorithm to build a biconnected subgraph with bottleneck edges
def BB_algorithm(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    H = nx.Graph()

    H.add_nodes_from(G.nodes())
    for u, v, data in edges_sorted:
        H.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(H):
            return H  # As soon as H is biconnected, return it

# Tour Identification
def find_hamiltonian_path(G):
    G_sq = nx.power(G, 2)
    all_paths = list(permutations(G.nodes()))
    min_max_weight = float('inf')
    optimal_path = None
    
    for path in all_paths:
        if path[0] == 0 and path[-1] == 0:  # path should start and end at the depot city
            max_weight = max((G_sq[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1)))
            if max_weight < min_max_weight:
                min_max_weight = max_weight
                optimal_path = path

    return optimal_attrs, min_max_weight

G = create_graph()
E_BB = BB_algorithm(G)
tour, max_distance = find_hamiltonian_path(E_BB)
total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print(f'Tour: {list(tour)}')
print(f'Total travel cost: {total_distance}')
print(f'Maximum distance between consecutive cities: {max_distance}')