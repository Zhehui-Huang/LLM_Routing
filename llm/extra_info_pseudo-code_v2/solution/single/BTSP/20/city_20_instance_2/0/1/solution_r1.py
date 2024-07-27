import math
import networkx as nx
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

def create_graph():
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=distance(i, j))
    return G

def find_minimum_bottleneck_hamiltonian_cycle(G):
    # Generating all permutations of nodes to find minimum bottleneck Hamiltonian cycle
    nodes = list(G.nodes())
    best_path = None
    min_bottleneck = float('inf')
    
    for permutation in permutations(nodes):
        if permutation[0] == 0:  # ensuring the tour starts at the depot
            max_edge_weight = max(G[permutation[i]][permutation[i+1]]['weight'] for i in range(len(permutation)-1))
            if max_edge_weight < min_bottleneck:
                best_path = permutation
                min_bottleneck = max_edge_weight
    
    # Close the cycle
    best_path += (best_path[0],)
    return best_path, min_bottleneck

G = create_graph()
tour, max_distance = find_minimum_bottleneck_hamiltonian_cycle(G)

# Calculating total distance
total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")