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
    c1, c2 = cities[city1], cities[city2]
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create a graph from given cities
G = nx.Graph()

# Adding nodes and edges between all pairs of cities
for c1 in cities:
    for c2 in cities:
        if c1 != c2:
            G.add_edge(c1, c2, weight=distance(c1, c2))

# Main function to apply BB algorithm and find an approximate BTSP tour
def solve_btsp(graph):
    edges_sorted_by_weight = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    biconnected_subgraph = nx.Graph()
    biconnected_subgraph.add_nodes_from(graph.nodes())
    
    for u, v, data in edges_sorted_by_weight:
        biconnected_subgraph.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(biconnected_subgraph):
            break

    # Tour identification
    biconnected_subgraph_square = nx.Graph()
    biconnected_subgraph_square.add_nodes_from(biconnected_subgraph.nodes())

    for u in biconnected_subgraph.nodes:
        for v in biconnected_subgraph.nodes:
            if u != v and nx.has_path(biconnected_subgraph, u, v):
                min_path_weight = min(data['weight'] for data in nx.all_simple_edge_paths(biconnected_subgraph, u, v))
                biconnected_subgraph_square.add_edge(u, v, weight=min_path_weight)

    # Find the Hamiltonian cycle using approximation
    cycle = nx.approximation.traveling_salesman_problem(biconnected_subgraph_square, cycle=True, method='greedy')
    
    # Calculate the max cost and total cost
    max_distance, total_cost = 0, 0
    for i in range(len(cycle) - 1):
        dist = distance(cycle[i], cycle[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    return cycle, total_cost, max_distance

# Solve BTSP
tour, total_cost, max_distance = solve_btsp(G)

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")