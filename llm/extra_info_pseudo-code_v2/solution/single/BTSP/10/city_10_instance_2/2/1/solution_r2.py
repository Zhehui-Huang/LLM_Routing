import math
import networkx as nx

# Definitions
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

# Compute Euclidean distance between two points
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate a list of edges sorted by distance
edges = [(i, j, distance(i, j)) for i in cities for j in cities if i < j]
edges.sort(key=lambda x: x[2])

# Create a graph from edge list
def create_graph_include_all_edges(nodes, edges):
    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    for u, v, d in edges:
        graph.add_edge(u, v, weight=d)
    return graph

# Use simple heuristic: Nearest Neighbor to find a tour
def nearest_neighbor_tour(graph, start_node):
    unvisited = set(graph.nodes)
    tour = [start_node]
    current = start_node
    unvisited.remove(start_node)
    tour_distance = 0
    max_edge_length = 0

    while unvisited:
        next_node = min(unvisited, key=lambda node: graph[current][node]['weight'])
        next_distance = graph[current][next_node]['weight']
        tour_distance += next_distance
        if next_distance > max_edge_length:
            max_edge_length = next_idstance
        tour.append(next_node)
        unvisited.remove(next_node)
        current = next_node

    # Closing the tour
    closing_distance = graph[tour[-1]][start_node]['weight']
    tour.append(start_node)
    tour_distance += closing_distance
    if closing_distance > max_edge_length:
        max_edge_length = closing_distance

    return tour, tour_distance, max_edge_length

# Main execution
graph = create_graph_include_all_edges(cities.keys(), edges)
tour, total_cost, max_distance = nearest_neighbor_tour(graph, 0)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")