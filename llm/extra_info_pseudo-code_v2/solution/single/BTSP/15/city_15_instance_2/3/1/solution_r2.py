import math
import networkx as nx

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def create_graph(cities):
    G = nx.complete_graph(len(cities))
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])
    return G

def find_biconnected_subgraph(G):
    sorted_edges = sorted(G.edges(data = True), key = lambda x: x[2]['weight'])
    BBG = nx.Graph()
    BBG.add_nodes_from(G)
    for edge in sorted_edges:
        u, v = edge[0], edge[1]
        BBG.add_edge(u, v)
        if nx.is_biconnected(BBG):
            break
    return BBG

def perform_tsp(G, nodes):
    weight_func = lambda u, v, data: data.get('weight', 1)
    tsp_tour = nx.approximation.traveling_salesman_problem(G, cycle=True, method=nx.approximation.christofides, weight=weight_func)
    return tsp_tour

def analyze_tour(tour, cities):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    # Closing the tour loop
    closing_distance = euclidean_distance(cities[tour[-1]], cities[tour[0]])
    total_distance += closing_distance
    max_distance = max(max_distance, closing_distance)
    return total_distance, max_distance

# Define cities
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Create graph and find biconnected subgraph
G = create_graph(cities)
BBG = find_biconnected_subgraph(G)

# Generate tour and analyze it
tsp_tour = perform_tsp(BBG, cities)
total_dist, max_consec_dist = analyze_tour(tsp_tour, cities)

# Outputs
print("Tour:", tsp_tour)
print("Total travel cost:", round(total_dist, 2))
print("Maximum distance between consecutive cities:", round(max_consec_dist, 2))