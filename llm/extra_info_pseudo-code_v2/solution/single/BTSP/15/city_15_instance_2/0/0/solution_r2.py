import math
import networkx as nx
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_complete_graph(coords):
    V = range(len(coords))
    G = nx.Graph()
    for i, j in combinations(V, 2):
        dist = euclidean_distance(coords[i], coords[j])
        G.add_edge(i, j, weight=dist)
    return G

def minimum_bottleneck_biconnected_subgraph(G):
    E = list(G.edges(data=True))
    E_sorted = sorted(E, key=lambda x: x[2]['weight'])

    for k in range(len(E_sorted)):
        Gr = nx.Graph()
        Gr.add_nodes_from(G.nodes)
        Gr.add_edges_from(E_sorted[:k+1], weight=1)  # include first k edges
        if nx.is_biconnected(Gr):
            bottleneck_weight = E_sorted[k][2]['weight']
            return Gr, bottleneckh_weight

def find_approximate_bottleneck_tour(G):
    cycle = list(nx.approximation.traveling_salesman_problem(G, cycle=True, weight='weight'))
    return cycle

def tour_distance_and_max_edge(tour, coords):
    total_cost = 0
    max_distance = 0
    n = len(tour)
    for i in range(n):
        dist = euclidean_distance(coords[tour[i]], coords[tour[(i+1) % n]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

# Input Coordinates
coords = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Creating a complete graph with distances
G = create_complete_graph(coords)

# Finding a bottleneck biconnected subgraph
G_biconnected, bottleneck_weight = minimum_bottleneck_biconnected_subgraph(G)

# Finding an approximate tour minimizing the maximum edge cost
tour = find_approximate_bottleneck_tour(G_biconnected)

# Calculating the total distance and maximum distance between consecutive nodes in the tour
total_cost, max_distance = tour_distance_and_max_edge(tour, coords)

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_date, 2))