import math
import itertools

# Data
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

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Compute distances and sort edges
edges = [(i, j, distance(i, j)) for i in cities for j in cities if i < j]
edges.sort(key=lambda x: x[2])

# Algorithm BB to find a bottleneck-optimal biconnected subgraph
def find_biconnected_subgraph(nodes, edges):
    from networkx import Graph, is_biconnected
    graph = Graph()
    graph.add_nodes_from(nodes)
    E_BB = []
    
    for u, v, d in edges:
        graph.add_edge(u, v, weight=d)
        if is_biconnected(graph):
            # Detect if current graph is biconnected
            edge_weights = [graph[u][v]['weight'] for u, v in graph.edges()]
            c_BB = max(edge_weights)
            return graph, c_BB, E_BB
        E_BB.append((u, v, d))
    return None, None, None  # Should not happen if correct data is given

# Get biconnected subgraph
b_graph, c_BB, E_BB = find_biconnected_subgraph(cities.keys(), edges)

# Generate an approximate optimal tour using the squared graph
def approximate_tour(graph):
    from networkx import shortest_path, all_pairs_shortest_path_length
    sqr_distances = all_pairs_shortest_path_length(graph)
    tour = []
    nodes = list(graph.nodes)
    # Implement a simple heuristic to make a Hamiltonian cycle: nearest neighbor
    current = nodes[0]
    remaining = set(nodes[1:])
    tour.append(current)

    while remaining:
        next_node = min(remaining, key=lambda x: sqr_distances[current][x])
        current = next_node
        tour.append(current)
        remaining.remove(current)

    tour.append(tour[0])  # Complete the cycle back to the depot
    return tour

# Identify the tour
tour = approximate_tour(b_graph)

# Calculate tour cost and find maximum distance between consecutive cities
total_cost = 0.0
max_distance = 0.0

for i in range(1, len(tour)):
    dist = distance(tour[i-1], tour[i])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Output the required data
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")