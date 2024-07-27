import math
import networkx as nx

# Define cities
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create fully-connected weighted graph
def create_weighted_graph(cities):
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)
    return G

def is_biconnected(G):
    return nx.is_biconnected(G)

# Heuristic algorithm implementation
def find_tsp_tour(cities):
    G = create_weighted_graph(cities)
    edges = list(G.edges(data=True))
    edges.sort(key=lambda x: x[2]['weight'])  # Sort edges by weight
    
    GB = nx.Graph()
    GB.add_nodes_from(G.nodes())
    E_BB = []

    # Step 0: Initialize solution set
    for edge in edges:
        GB.add_edge(*edge[0:2], weight=edge[2]['weight'])
        E_BB.append(edge)
        if is_biconnected(GB):
            break
    
    # Tour Identification in G^2
    squares = nx.power(GB, 2)
    cycle = nx.approximation.traveling_salesman_problem(squares, weight='weight')
    final_tour = [cycle[0]] + cycle + [cycle[0]]  # Ensure it starts and ends at the depot
    cycle_dist = calculate_tour_distances(final_tour, cities)
    total_cost = sum(cycle_dist)
    max_dist = max(cycle_dist)
    
    return final_tour, total_cost, max_dist

def calculate_tour_distances(tour, cities):
    distances = []
    for i in range(len(tour) - 1):
        distances.append(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]))
    return distances

# Perform the algorithm
tour, total_cost, max_dist = find_tsp_tour(cities)
print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost}')
print(f'Maximum distance between consecutive cities: {max_dist}')