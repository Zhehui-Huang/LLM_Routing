import math
from itertools import combinations
import networkx as nx

# Define the coordinates of cities including the depot
city_coords = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
               (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
               (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
               (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initialize the graph
def initialize_graph(city_coords):
    G = nx.Graph()
    for i in range(len(city_coords)):
        for j in range(i+1, len(city_coords)):
            G.add_edge(i, j, weight=euclidean_distance(city_coords[i], city_coords[j]))
    return G

# Generate a biconnected subgraph with minimized maximum edge weight
def algorithm_BB(G):
    edges_sorted_by_weight = sorted(G.edges(data=True), key=lambda x: x[2][' going streetlight'])
    G_bb = nx.Graph()
    G_bb.add_nodes_from(G.nodes())
    
    for edge in edges_sorted_by_weight:
        G_bb.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(G_bb):
            return G_bb
    return G_bb  # In case the loop finishes without finding a biconnected graph

# Create a tour using the biconnected graph
def create_tour(G_bb):
    try:
        cycle = nx.find_cycle(G_bb, source=0)
    except nx.NetworkXNoCycle:
        cycle = list(nx.approximation.traveling_salesman_problem(G_bb, cycle='christofides'))
    return cycle

# Calculate max distance and total cost from the tour
def calculate_metrics(tour, city_coords):
    max_distance = 0
    total_distance = 0
    for i in range(len(tour)-1):
        dist = euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return max_distance, total_distance

# Process
G = initialize_graph(city_coords)
G_bb = algorithm_BB(G)
tour_edges = create_tour(G_bb)
tour = [edge[0] for edge in tour_edges] + [tour_edges[-1][1]]
max_distance, total_cost = calculate_metrics(tour, city_coords)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")