import itertools
import math
import networkx as nx

# Definition of city coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99),
    (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Create a complete graph from city coordinates
def create_graph(cities):
    G = nx.Graph()
    number_of_cities = len(cities)
    for i in range(number_of_cities):
        for j in range(i + 1, number_of_cities):
            dist = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)
    return G

# Generate a biconnected subgraph by adding the least weight edges that keep the graph biconnected
def algorithm_bb(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    biconnected_subgraph = nx.Graph()
    for (u, v, data) in sorted_edges:
        biconnected_subgraph.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(biconnected_subgraph):
            break
    return biconnected_subgraph

# Use Christofides algorithm to find a tour in weighted graph that visits every vertex at least once
def find_tour(G):
    # MST using Kruskal's algorithm
    T = nx.minimum_spanning_tree(G, weight='weight')
    # Multigraph that will contain the MST and minimum matching on odd-degree nodes
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]
    min_weight_matching = nx.algorithms.matching.min_weight_matching(G.subgraph(odd_degree_nodes), maxcardinality=True, weight='weight')
    T.add_edges_from(min_weight_matching)
    # Find an Eulerian circuit in the multigraph
    eulerian_circuit = list(nx.eulerian_circuit(nx.MultiGraph(T), source=0))
    path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # Complete the cycle
    return path

# Function to calculate traveling cost and max edge length
def travel_info(path, G):
    edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    total_cost = sum(G[u][v]['weight'] for u, v in edges)
    max_edge_length = max(G[u][v]['weight'] for u, v in edges)
    return total_cost, max_edge_length

# Execution of defined functions
G = create_graph(cities)
G_bb = algorithm_bb(G)
tour = find_tour(G_bb)
total_cost, max_distance = travel_info(tour, G)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")