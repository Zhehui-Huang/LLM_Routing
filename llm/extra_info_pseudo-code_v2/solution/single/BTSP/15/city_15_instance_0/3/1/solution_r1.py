import math
import networkx as nx
from itertools import permutations

# Coordinates of cities with the depot as the first entry
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23),
    (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def find_biconnected_subgraph(cities):
    """ Heuristic for finding a biconnected subgraph with minimizing max edge weight """
    num_cities = len(cities)
    G = nx.Graph()
    G.add_nodes_from(range(num_cities))
    
    # Sorting edges by ascending distance
    edges_sorted_by_distance = sorted(
        [(i, j, euclidean_distance(cities[i], cities[j])) for i in range(num_cities) for j in range(i + 1, num_cities)],
        key=lambda x: x[2]
    )
    
    # Adding edges until the graph is biconnected
    for i, j, dist in edges_sorted_by_distance:
        G.add_edge(i, j, weight=dist)
        if nx.is_biconnected(G):
            break
    
    return G

def find_approximate_tsp_tour(G, cities):
    """ Find a TSP tour through permutation and checking on biconnected graph, minimizing max edge """
    min_max_distance = float('inf')
    best_tour = None
    
    for tour in permutations(range(1, len(cities))):
        tour = (0,) + tour + (0,)  # ensure starts and end at the depot
        max_edge_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        if max_edge_distance < min_max_distance:
            min_max_distance = max_edge_distance
            best_tour = tour
            
    total_cost = sum(euclidean_distance(cities[best_tour[i]], cities[best_tour[i+1]]) for i in range(len(best_tour) - 1))
    
    return best_tour, total_cost, min_max_distance

# Generate biconnected subgraph
G = find_biconnected_subgraph(cities)
# Find TSP tour from a biconnected graph
tour, total_cost, max_distance = find_approximate_tsp_tour(G, cities)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)