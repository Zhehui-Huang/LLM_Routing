import math
import networkx as nx

# Data (coordinates of each city)
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Distance calculation function
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a complete graph with cities and edges weighted by Euclidean distance
def create_complete_graph(city_coordinates):
    G = nx.complete_graph(len(city_coordinates))
    for i in range(len(city_coordinates)):
        for j in range(i + 1, len(city_coordinates)):
            distance = calc_distance(city_coordinates[i], city_coordinates[j])
            G[i][j]['weight'] = distance
    return G

# Check if graph G is biconnected
def is_biconnected(G):
    return nx.is_biconnected(G)

# Algorithm to generate biconnected subgraph with bottleneck optimal property
def bottleneck_biconnected_subgraph(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    BB = nx.Graph()
    BB.add_nodes_from(G.nodes())
    for edge in edges_sorted:
        BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if is_biconnected(BB):
            return BB
    return BB

# Pseudocode for solving problem
def solve_btsp(G):
    step1_subgraph = bottleneck_biconnected_subgraph(G)
    tour = list(nx.approximation.traveling_salesman_problem(step1_subgraph, cycle=True, method='greedy'))
    tour.append(tour[0])  # Making it a cycle

    total_distance = 0
    max_distance = 0
    prev_city = tour[0]
    for city in tour[1:]:
        dist = G[prev_city][city]['weight']
        total_distance += dist
        max_distance = max(max_distance, dist)
        prev_model = city

    return tour, total_distance, max_distance

# Running the code
G = create_complete_graph(cities)
tour, total_cost, max_leg_distance = solve_btsp(G)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_gain_distance)