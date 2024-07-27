import math
import networkx as nx

# Define city coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create and build the graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Find a biconnected component that includes the depot
def find_biconnected_component_with_depot(graph, depot):
    for component in nx.biconnected_components(graph):
        if depot in component:
            subgraph = graph.subgraph(component)
            return subgraph
    return None

# Adding all edges and then ensuring the graph is biconnected
def create_biconnected_graph(graph):
    sorted_edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    bcc = nx.Graph()
    bcc.add_nodes_from(graph.nodes())
    for u, v, data in sorted_edges:
        bcc.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(bcc):
            return bcc
    return bcc  # In case all edges are needed

# Finding tour with minimum maximum edge
def find_minimum_maximum_tour(graph):
    bcc_graph = create_biconnected_graph(graph)
    cycle = nx.approximation.traveling_salesman_problem(bcc_graph, cycle=True, weight='weight')
    max_edge = max(bcc_graph[u][v]['weight'] for u, v in zip(cycle[:-1], cycle[1:]) + [(cycle[-1], cycle[0])])
    total_distance = sum(bcc_graph[u][v]['weight'] for u, v in zip(cycle[:-1], cycle[1:]) + [(cycle[-1], cycle[0])])
    return cycle, total_distance, max_edge

tour, total_cost, max_distance = find_minimum_maximum_tour(G)

# Output result
print("Tour:", tour)
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")