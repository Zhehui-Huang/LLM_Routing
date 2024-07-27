import networkx as nx
import math
from itertools import combinations

def calculate_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define coordinates of cities
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Create a complete graph
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i+1, len(cities)):
        G.add_edge(i, j, weight=calculate_distance(cities[i], cities[j]))

# Determine the bottleneck biconnected subgraph
def find_biconnected_bottleneck_subgraph(G):
    """Find a bottleneck biconnected subgraph."""
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    subG = nx.Graph()
    subG.add_nodes_from(G.nodes)
    for u, v, _ in sorted_edges:
        subG.add_edge(u, v)
        if nx.is_biconnected(subG):
            return subG
    return subG  # This line is generally unreachable

biconnected_subgraph = find_biconnected_bottleneck_subgraph(G)

# Find a tour minimizing the maximum edge cost
def find_minimax_path(G):
    """Find a path that minimizes the maximum edge in a cycle."""
    best_tour = None
    best_max_edge = float('inf')
    total_cost = 0
    for cycle in nx.simple_cycles(nx.complete_graph(G)):
        if len(cycle) == nx.number_of_nodes(G) + 1:  # Look for Hamiltonian cycles, that is full cycle plus return to start
            max_edge = max(G[cycle[i]][cycle[i+1]]['weight'] for i in range(len(cycle)-1))
            if max_edge < best_max_edge:
                best_max_edge = max_edge
                best_tour = cycle
                total_cost = sum(G[cycle[i]][cycle[i+1]]['weight'] for i in range(len(cycle)-1))
    return best_tour, total_cost, best_max_edge

tour, cost, max_distance = find_minimax_path(biconnected_subgraph)

# Output the final results
print("Tour:", tour)
print("Total travel cost:", cost)
print("Maximum distance between consecutive cities:", max_distance)