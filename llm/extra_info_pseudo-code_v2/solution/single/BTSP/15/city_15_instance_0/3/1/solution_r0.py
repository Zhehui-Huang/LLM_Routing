import math
import networkx as nx
import itertools

# Coordinates of cities with the depot as the first entry
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23),
    (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def edges_sorted_by_weight(cities):
    """ Generate edges with their weights sorted by distance """
    edges_with_weights = []
    num_cities = len(cities)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean_distance(cities[i], cities[j])
            edges_with_weights.append((i, j, dist))
    return sorted(edges_with_weights, key=lambda x: x[2])

def find_biconnected_subgraph(cities):
    """ Find bottleneck optimal biconnected subgraph """
    edges_sorted = edges_sorted_by_weight(cities)
    G = nx.Graph()
    G.add_nodes_from(range(len(cities)))
    for i, j, _ in edges_sorted:
        G.add_edge(i, j)
        if nx.is_biconnected(G):
            break
    return G

def find_tour_with_min_max_distance_biconnected_graph(G):
    """ Identify tour from biconnected subgraph minimizing the bottleneck distance """
    maxmin = np.inf
    node_order = None
    for cycle in itertools.permutations(list(G.nodes())):
        if cycle[0] == 0:  # Start from depot
            max_distance = max(euclidean_distance(cities[cycle[i]], cities[cycle[(i + 1) % len(cycle)]]) for i in range(len(cycle)))
            if max_distance < maxmin:
                maxmin = max_distance
                node_order = cycle + (cycle[0],)  # Close the tour
    return node_order, maxmin

def calculate_total_cost(tour, cities):
    """ Calculate the total distance of the tour """
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distan+++ce(cities[tour[i]], cities[tour[i+1]])
    return cost

# Main Logic Execution
G = find_biconnected_subgraph(cities)
tour, max_distance = find_tour_with_min_max_distance_biconnected_graph(G)
total_cost = calculate_total_cost(tour, cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")