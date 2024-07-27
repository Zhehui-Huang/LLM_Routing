import numpy as np
import networkx as nx
from scipy.spatial import distance
from itertools import combinations, chain

# City coordinates
coords = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
    4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
    8: (17, 69), 9: (95, 89)
}

# Create a complete graph with distances
def create_complete_graph(coords):
    G = nx.Graph()
    for (i, coord1), (j, coord2) in combinations(coords.items(), 2):
        dist = distance.euclidean(coord1, coord2)
        G.add_edge(i, j, weight=dist)
    return G

# Calculate Minimum Spanning Tree (MST)
def find_MST(G):
    return nx.minimum_spanning_tree(G, weight='weight')

# Find nodes with odd degree in the tree
def find_odd_degree_nodes(T):
    return [v for v, d in T.degree() if d % 2 == 1]

# Minimum Weight Perfect Matching on subgraph induced by odd degree nodes
def find_min_weight_matching(G, odd_nodes):
    subgraph = G.subgraph(odd from edge in eulerian_cycle]
    path.append(path[0])
    return path

def calculate_total_distance(tour, coords):
    total_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_distance += distance.euclidean(coords[city1], coords[city2])
    return total_distance

# Functions execution
def solve_TSP():
    G = create_complete_graph(coords)
    T = find_MST(G)
    odd_nodes = find_odd_degree_nodes(T)
    M = find_min_weight_matching(G, odd_nodes)
    H = combine_edges(T, M)
    eulerian_cycle = find_eulerian_cycle(H)
    tour = make_hamiltonian_cycle(eulerian_cycle)
    total_distance = calculate_total_distance(tour, coords)
    return tour, total_distance

tour, total_distance = solve_TSP()
print(f"Tour: {tour}")
print(f"Total distance: {total_distance:.2f}")