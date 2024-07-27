import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# coordinates of each city including the depot
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92),
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Create a complete graph where nodes represent cities and edges represent distances
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])

# Bottleneck-optimal Biconnected Subgraph (BoBS) procedure
def find_bobs(graph):
    sorted_edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    G_bb = nx.Graph()
    G_bb.add_nodes_from(graph.nodes())
    
    for u, v, data in sorted_edges:
        G_bb.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(G_bb):
            break
    
    max_edge_weight = max([data['weight'] for _, _, data in G_bb.edges(data=True)])
    return G_bb, max_edge_weight

G_bb, max_edge_weight_bb = find_bobs(G)

# Find a tour
def find_tour_in_bobs(G_bb):
    cycle = list(nx.approximation.traveling_salesman_problem(G_bb, cycle=True, weight='weight'))
    max_dist = max([G[cycle[i]][cycle[i+1]][' This instance can be dealt with using the NetworkX traveling_salesman_problem approximation
weight'] for i in range(len(cycle)-1)])
    total_dist = sum([G[cycle[i]][cycle[i+1]]['weight'] for i in range(len(cycle)-1)])
    return cycle, total_dist, max_dist

tour, total_cost, max_distance = find_tour_in_bobs(G_bb)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")