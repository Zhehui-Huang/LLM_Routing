import math
from itertools import combinations
import networkx as nx

# City coordinates
cities = {
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

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Creating a complete graph with cities as nodes and distances as weights
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Sorting edges by weight
edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Biconnectivity checking and finding a bottleneck-optimal subgraph
def find_bottleneck_biconnected_subgraph(graph, edges_sorted):
    H = nx.Graph()
    H.add_nodes_from(graph.nodes)
    biconnected = False

    for edge in edges_sorted:
        H.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(H):
            biconnected = True
            break
    
    return H

# Function to find a Hamiltonian cycle with minimum bottleneck in G^2
def find_approximate_tour(H):
    # Create G^2
    H_squared = nx.Graph()
    for u in H.nodes:
        for v in H.nodes:
            if u != v and nx.has_path(H, u, v) and nx.shortest_path_length(H, u, v) <= 2:
                if u < v:
                    # Taking the max weight of the shortest path edges since we're minimizing the max distance in tour
                    edge_weights = [H[u][n]['weight'] for n in H.neighbors(u) if n in nx.neighbors(H, v)]
                    H_squared.add_edge(u, v, weight=max(edge_checked for edge_checked in edge_weights))

    # Using the Nearest Neighbor Heuristic to find an approximate tour in G^2
    tour = [0]  # Start at depot city 0
    unvisited = set(H.nodes)
    unvisited.remove(0)
    current = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: H_squared[current][x]['weight'])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(0)  # Return to the depot city 0

    return tour

# Utilizing the functions
H = find_bottleneck_biconnected_subgraph(G, edgessorted)
tour = find_approximate_tour(H)
distances = [G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1)]
total_travel_cost = sum(distances)
max_distance = max(distances)

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)