import math
import networkx as nx
from networkx.algorithms import approximation

# Compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Building a complete graph
def build_graph(cities):
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

# Heuristic to find an approximate tour minimizing the maximum distance in the tour
def find_approximate_minimax_tour(G):
    # Using 2-approximation of minimum spanning tree and making it a tour
    mst = nx.minimum_spanning_tree(G, weight='weight')
    doubled_mst = nx.MultiGraph(mst)
    doubled_mst.add_edges_from(mst.edges)
    euler_circuit = list(nx.eulerian_circuit(nx.eulerize(doubled_mst)))
    
    tour = []
    visited = set()
    max_edge_weight = 0
    
    for u, v in euler_circuit:
        if u not in visited:
            visited.add(u)
            tour.append(u)
            if len(tour) > 1:
                weight = G[tour[-2]][tour[-1]]['weight']
                max_edge_weight = max(max_edge_weight, weight)
    
    # Closing the tour
    tour.append(tour[0])
    final_edge_weight = G[tour[-2]][tour[-1]]['weight']
    max_edge_weight = max(max_edge_weight, final_edge_weight)
    
    return tour, max_edge_weight

# Calculate total travel cost and maximum distance between consecutive cities
def calculate_metrics(cities, tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += distance
        max_distance = max(max_distance, distance)
    return total_cost, max_distance

# Defining cities
cities = [
    (53, 68), (75, 11), (91, 95), (22, 80), (18, 63),
    (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)
]

# Main execution
G = build_graph(cities)
tour, bottleneck = find_approximate_minimax_tour(G)
total_cost, max_consecutive_distance = calculate_metrics(cities, tour)

print("Tour:", tour)
print("Bottleneck (longest edge in tour):", bottleneck)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)