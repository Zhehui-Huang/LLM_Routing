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

# Generate a complete graph G with weights as Euclidean distances
G = nx.complete_graph(len(cities))
for i in cities:
    for j in cities:
        if i != j:
            G[i][j]['weight'] = euclidean_distance(i, j)

# Biconnected Graph Construction
def algorithm_bb(graph):
    edges_sorted = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    biconnected_subgraph = nx.Graph()
    biconnected_subgraph.add_nodes_from(graph.nodes())
    for edge in edges_sorted:
        biconnected_subgraph.add_edge(*edge[:2], weight=edge[2]['weight'])
        if nx.is_biconnected(biconnected_subgraph):
            return biconnected_subgraph
    return biconnected_subgraph

# Obtaining a bottleneck-optimal biconnected subgraph
E_BB = algorithm_bb(G)

# Create the square of the graph
E_BB_square = nx.power(E_BB, 2)

# Finding a Hamiltonian cycle, using networkx approximation (this needs the graph to be complete)
tour = nx.approximation.traveling_salesman_problem(E_BB_square, cycle=True)

# Calculate total travel cost and max distance
def calculate_metrics(tour, graph):
    total_cost = 0
    max_dist = 0
    for i in range(len(tour) - 1):
        dist = graph[tour[i]][tour[i + 1]]['weight']
        total_cost += dist
        if dist > max_dist:
            max_dist = dist
    # Include the return to start
    return_to_start_dist = graph[tour[-1]][tour[0]]['weight']
    total_cost += return_to_start_dist
    max_dist = max(max_dist, return_to_start_dist)
    return total_cost, max_dist

total_cost, max_distance = calculate_metrics(tour, G)

# Displaying the output as specified
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)