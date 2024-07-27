import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def make_graph(nodes):
    n = len(nodes)
    graph = {}
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distanace(nodes[i], nodes[j])
            graph[(i, j)] = dist
            graph[(j, i)] = dist
    return graph

def is_biconnected(graph, n):
    from networkx import Graph, is_biconnected
    G = Graph()
    G.add_nodes_from(range(n))
    G.add_weighted_edges_from((u, v, w) for (u, v), w in graph.items() if w > 0)
    return is_biconnected(G)

def find_bottleneck_spanning_tree(nodes):
    n = len(nodes)
    graph = make_graph(nodes)
    sorted_edges = sorted(graph.items(), key=lambda x: x[1])
    b_graph = {}

    for (i, j), d in sorted_edges:
        b_graph[(i, j)] = d
        b_graph[(j, i)] = d
        if is_biconnected(b_graph, n):
            break
        else:
            b_graph[(i, j)] = b_graph[(j, i)] = 0

    return b_graph, max(b_graph.values()) if b_graph else float('inf')

def tour_from_biconnected(graph, n):
    tour = [0]  # Start at the depot
    visited = set(tour)
    current = 0
    
    while len(tour) < n:
        next_edge = min(((v, w) for k, w in graph.items() if k[0] == current and v not in visited and w > 0), key=lambda x: x[1])
        next_node = next_edge[0][1]
        tour.append(next_node)
        visited.add(next_node)
        current = next_node

    tour.append(0)  # Return to the depot
    return tour

def calculate_tour_cost(tour, distances):
    total_cost = 0
    max_distance = 0

    for i in range(len(tour) - 1):
        distance = distances[(tour[i], tour[i+1])]
        total_cost += distance
        max_distance = max(max_distance, distance)

    return total_cost, max_distance

city_coords = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Step 1: Compute the Bottleneck-optimal Biconnected Subgraph
b_graph, max_bottleneck = find_bottleneck_spanning_tree(city_coords)

# Step 2: Construct a tour from the biconnected subgraph
tour = tour_from_biconnected(b_graph, len(city_coords))

# Calculate cost and max distance
spaces_distances = make_graph(city_coords)
total_cost, max_distance = calculate_tour_cost(tour, spaces_distances)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")