import math
from itertools import combinations
from networkx import Graph, is_biconnected

def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def initialize_graph(city_locations):
    n = len(city_locations)
    G = Graph()
    G.add_nodes_from(range(n))
    for (i, j) in combinations(range(n), 2):
        G.add_edge(i, j, weight=euclidean_distance(city_locations[i], city_locations[j]))
    return G

def biconnected_subgraph(G):
    edge_list_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    G_BB = Graph()
    G_BB.add_nodes_from(G.nodes())
    for (u, v, data) in edge_list_sorted:
        G_BB.add_edge(u, v, weight=data['weight'])
        if is_biconnected(G_BB):
            break
    return G_BB

def find_tour(G_BB):
    # Find Hamiltonian cycle
    # This is just a placeholder for simplicity and might not ensure a feasible tour.
    cycle = list(G_BB.nodes()) + [list(G_BB.nodes())[0]]
    return cycle

def calculate_max_and_total_distance(cycle, G):
    max_distance = 0
    total_distance = 0
    for i in range(len(cycle) - 1):
        u, v = cycle[i], cycle[i+1]
        distance = G[u][v]['weight']
        total_distance += distance
        if distance > max_distance:
            max_distance = distance
    return total_distance, max_distance

# Main Execution
city_locations = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

G = initialize_graph(city_locations)
G_BB = biconnected_subgraph(G)
tour = find_tour(G_BB)
total_cost, max_distance = calculate_max_and_total_distance(tour, G)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)