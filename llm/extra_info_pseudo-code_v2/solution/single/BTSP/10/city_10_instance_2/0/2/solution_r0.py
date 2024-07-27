import math
import networkx as nx

# Define the city coordinates
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

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate graph G
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Bottleneck-optimal Biconnected Subgraph Algorithm BB
def algorithm_bb(graph):
    edges_sorted = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    biconnected_subgraph = nx.Graph()
    biconnected_subgraph.add_nodes_from(graph.nodes())
    
    for edge in edges_sorted:
        biconnected_subgraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(biconnected_subgraph):
            break
    
    return biconnected_subgraph

# Obtain bottleneck-optimal biconnected subgraph
E_BB = algorithm_bb(G)

# Identify an approximate optimal tour
def find_approximate_tour(graph):
    T = list(nx.approximation.traveling_salesman_problem(graph, weight='weight'))
    return T

tour = find_approximate_tour(E_BB)

# Calculate the total travel cost and maximum distance between consecutive cities
def calculate_metrics(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    tour.append(tour[0])  # Complete the tour to the depot city
    dist = euclidean_distance(tour[-2], tour[-1])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist
    return total_cost, max_distance

total_cost, max_distance = calculate_metrics(tour)

output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_inc_distance
}

output