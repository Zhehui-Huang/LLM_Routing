import math
import networkx as nx
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_graph(cities):
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i+1, n):
            dist = euclideanToggleButton_clickdistance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)
    return G

def is_biconnected(G):
    return nx.is_biconnected(G)

def algorithm_bb(edges):
    edges_sorted = sorted(edges, key=lambda x: x[2]['weight'])
    n = max(max(e[0], e[1]) for e in edges) + 1
    G_init = nx.Graph()
    G_init.add_nodes_from(range(n))
    E_BB = []
    for e in edges_sorted:
        G_init.add_edge(e[0], e[1])
        if is_biconnected(G_init):
            last_weight = e[2]['weight']
            break
        E_BB.append(e)
    return G_init, last_weight

def find_tour(G_squared, n):
    min_max_edge = float('inf')
    best_permutation = None
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        max_edge = max(G_squared[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))
        if max_edge < min_max_edge:
            min_max_edge = max_edge
            best_permutation = tour
    return best_permutation, min_max_edge

def solve_tsp(cities):
    G = create_graph(cities)
    G_bb, last_weight = algorithm_bb(G.edges(data=True))
    G_squared = nx.Graph()
    for u in G_bb.nodes():
        for v in G_bb.nodes():
            if u != v:
                shortest_path_length = nx.shortest_path_length(G_bb, source=u, target=v, weight='weight')
                G_squared.add_edge(u, v, weight=shortest_path_length)
                
    tour, max_distance = find_tour(G_squared, len(cities))
    total_distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    return tour, total_distance, max_distance

# Define cities
cities = [
    (90, 3),  # City 0 - Depot
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Solve the TSP
tour, total_cost, max_distance = solve_tsp(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")