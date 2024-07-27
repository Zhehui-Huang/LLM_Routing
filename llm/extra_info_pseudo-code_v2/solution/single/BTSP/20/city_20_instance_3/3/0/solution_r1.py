import math
from itertools import combinations
import networkx as nx

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def create_graph(cities):
    graph = nx.Graph()
    n = len(cities)
    for idx1 in range(n):
        for idx2 in range(idx1 + 1, n):
            weight = euclidean_distance(cities[idx1], cities[idx2])
            graph.add_edge(idx1, idx2, weight=weight)
    return graph

def bottleneck_optimal_biconnected_subgraph(graph):
    sorted_edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    biconnected_subgraph = nx.Graph()
    biconnected_subgraph.add_nodes_from(graph.nodes())
    max_biconnect_edge_weight = 0
    for u, v, data in sorted_edges:
        biconnected_subgraph.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(biconnected_subgraph):
            max_biconnect_edge_weight = data['weight']
            if all(nx.has_path(biconnected_subgraph, u, v) for u in biconnected_subgraph for v in biconnected_subgraph):
                # As soon as the subgraph is biconnected and all nodes are accessible, stop adding more edges.
                break
    return biconnected_subgraph, max_biconnect_edge_weight

def compute_tour(graph):
    tour = nx.approximation.traveling_salesman_problem(graph, cycle=True, weight='weight', method='greedy')
    return tour

cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Initialize graph
graph = create_graph(cities)

# Find bottleneck-optimal biconnected subgraph
biconnected_subgraph, max_biconnect_edge_weight = bottleneck_optimal_biconnected_subgraph(graph)

# Compute Tour
tour = compute_tour(biconnected_subgraph)

# Calculate total cost and max distance in the tour:
total_cost = sum(graph.edges[tour[i], tour[i + 1]]['weight'] for i in range(len(tour) - 1))
max_distance = max(graph.edges[tour[i], tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Ensure the tour starts and ends at the depot city (0)
if tour[0] != 0:
    # Rotate tour to start at 0
    zero_index = tour.index(0)
    tour = tour[zero_index:] + tour[:zero_index]

# Ensure tour is cyclic by repeating the start node
tour.append(tour[0])

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")