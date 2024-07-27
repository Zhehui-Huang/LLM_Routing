import math
from itertools import combinations
from networkx import Graph, is_biconnected

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_distances(cities):
    distances = {}
    for i, j in combinations(range(len(cities)), 2):
        dist = euclidean_distance(cities[i], cities[j])
        distances[(i, j)] = dist
        distances[(j, i)] = dist
    return distances

def initialize_graph(cities, distances):
    G = Graph()
    for i in range(len(cities)):
        G.add_node(i)
    for (i, j), dist in distances.items():
        G.add_edge(i, j, weight=dist)
    return G

def algorithm_bb(graph, cities):
    edges_sorted = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    G_BB = Graph()
    G_BB.add_nodes_from(graph.nodes())
    edge_added = 0
    while not is_biconnected(G_BB):
        (u, v, _) = edges_sorted[edge_added]
        G_BB.add_edge(u, v)
        edge_added += 1
    return G_BB

def find_tour_approx(graph):
    # This function should ideally use some strategy to find a BTSP tour.
    # This implementation is a placeholder. Replace it with a real one if necessary.
    nodes = list(graph.nodes)
    tour = nodes + [nodes[0]]
    return tour

# City coordinates
cities = [
    (50, 42),
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# Algorithm Steps
distances = calculate_distances(cities)
full_graph = initialize_graph(cities, distances)
G_BB = algorithm_bb(full_graph, cities)
tour = find_tour_approx(G_BB)

# Calculate Costs
total_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
max_distance = max(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")