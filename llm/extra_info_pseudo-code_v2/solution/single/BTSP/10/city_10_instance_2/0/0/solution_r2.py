import math
import networkx as nx
from itertools import permutations

# City coordinates: index => (x, y)
coordinates = {
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

# Calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create a complete graph with weighted edges based on distances
def create_complete_graph(coordinates):
    G = nx.Graph()
    for i in coordinates:
        for j in coordinates:
            if i != j:
                G.add_edge(i, j, weight=euclideanly_distance(coordinates[i], coordinates[j]))
    return G

G = create_complete_graph(coordinates)

# Algorithm BB: Bottleneck-Optimal Biconnected Subgraph
def algorithm_bb(graph):
    sorted_edges = sorted(graph.edges(data=True), key=lambda e: e[2]['weight'])
    bb_graph = nx.Graph()

    for (u, v, data) in sorted_edges:
        bb_graph.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(bb_graph):
            return bb_graph

# Step 1: Using Algorithm BB from pseudocode
G_bb = algorithm_bb(G)

# Finding a biconnected subgraph's square
def graph_square(G):
    G2 = nx.Graph()
    for u in G.nodes():
        for v in G.nodes():
            if u != v and nx.shortest_path_length(G, u, v, weight='weight') <= 2:
                G2.add_edge(u, v, weight=max(nx.get_edge_attributes(G, 'weight').get((u, v), 0), nx.get_edge_attributes(G, 'weight').get((v, u), 0)))
    return G2

G2 = graph_square(G_bb)

# Step 2: Create a Hamiltonian tour in G2
def find_tour(G2, start_node=0):
    # Try all permutations keeping the start node fixed
    paths = permutations([n for n in G2.nodes() if n != start_node])
    min_max_weight = float('inf')
    best_path = None
    
    for path in paths:
        path = (start_node,) + path + (start_node,)
        max_weight = max(G2[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
        if max_weight < min_max_weight:
            min_max_weight = max_weight
            best_path = path
    
    return best_path, min_max_weight

tour, max_edge_weight = find_tour(G2)

# Compute tour details
def tour_cost_details(tour):
    total_cost = sum(G[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))
    return total_cost

total_cost = tour_cost_details(tour)

# Output the results correctly this time
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_edge_weight}")