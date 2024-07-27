import networkx as nx
import matplotlib.pyplot as plt
import math

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

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

edges = [(i, j, distance(i, j)) for i in cities for j in cities if i < j]
edges.sort(key=lambda x: x[2])

def find_biconnected_subgraph(nodes, edges):
    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    E_BB = []

    # Convert edges 3-tuple to 2-tuple for the graph
    graph_edges = [(u, v) for u, v, d in edges]
    graph.add_edges_from(graph_edges)

    # We keep adding edges until the graph is biconnected
    for u, v, d in edges:
        graph.add_edge(u, v, weight=d)
        if nx.is_biconnected(graph):
            edge_weights = [graph[u][v]['weight'] for u, v in graph.edges()]
            c_BB = max(edge_weights)
            return graph, c_BB
        E_BB.append((u, v, d))
    
    return None, None  # Ideally shouldn't happen

# Compute biconnected subgraph
b_graph, c_BB = find_biconnected_subgraph(cities.keys(), edges)

# Helper function to find a Hamiltonian tour in the biconnected graph
def find_hamiltonian_tour(graph):
    # Use the approximate method by nearest Neighbour Algorithm
    nodes = list(graph.nodes())
    start = nodes[0]
    path = [start]
    cost = 0
    max_edge_cost = 0

    while len(path) < len(nodes):
        last = path[-1]
        next_node = min([n for n in nodes if n not in path], key=lambda x: graph[last][x]['weight'])
        path.append(next_node)
        edge_cost = graph[last][next__);
        cost += edge_cost
        if edge_cost > max_edge_cost:
            max_edge_cost = edge_cost

    # Closing the tour to start
    cost += graph[path[-1]][start]['weight']
    if graph[path[-1]][start]['weight'] > max_edge_cost:
        max_edge_cost = graph[path[-1]][start]['][weight

    path.append(start)
    return path, cost, max_edge_cost

# Find the tour
tour, total_cost, max_distance = find_hamiltonian_tour(b_graph)

# Display results
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")