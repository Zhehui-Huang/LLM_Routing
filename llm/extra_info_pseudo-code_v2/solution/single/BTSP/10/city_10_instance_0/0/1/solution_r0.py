import math
from itertools import combinations
import networkx as nx

# Given city coordinates
cities = [
    (50, 42), # Depot 0
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

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create a complete graph with weighted edges (distances between cities)
def create_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            dist = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)
    return G

# Bottleneck-optimal biconnected subgraph using algorithm BB
def find_biconnected_subgraph(G):
    edges_sorted_by_weight = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    BB = nx.Graph()
    BB.add_nodes_from(G.nodes())
    
    for u, v, data in edges_sorted_by_weight:
        BB.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(BB):
            break
    
    max_weight = max([data['weight'] for u, v, data in BB.edges(data=True)])
    return BB, max_weight

# Construct an approximate optimal tour using biconnected subgraph
def find_approximate_tour(BB):
    # Create the square of the graph
    G_squared = nx.Graph()
    for u in BB.nodes():
        G_squared.add_node(u)
    
    for u, v in combinations(BB.nodes(), 2):
        if nx.has_path(BB, u, v) and nx.shortest_path_length(BB, u, v) <= 2:
            short_path = nx.shortest_path(BB, u, v)
            weight = BB.edges[short_path[0], short_path[1]]['weight']
            G_squared.add_edge(u, v, weight=weight)
    
    # Use the shortest path heuristic: nearest neighbor
    tour = list(nx.approximation.traveling_salesman_problem(G_squared, cycle=True))
    
    # Calculate the total cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour)):
        j = (i + 1) % len(tour)
        dist = euclidean_distance(cities[tour[i]], cities[tour[j]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return tour, total_cost, max_distance

# Main execution
graph = create_graph(cities)
subgraph, max_edge_weight = find_biconnected_subgraph(graph)
tour, total_cost, max_distance = find_approximate_tour(subgraph)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")