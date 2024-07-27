import math
import networkx as nx
from itertools import combinations

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def create_biconnected_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    G_BB = nx.Graph()
    G_BB.add_nodes_from(G)
    
    for edge in edges_sorted:
        u, v, _ = edge
        G_BB.add_edge(u, v)
        if nx.is_biconnected(G_BB):
            break
    
    return G_BB

def approximate_tour(G_BB, origin):
    # Using the Christofides algorithm to generate an approximate tour
    tour = list(nx.approximation.traveling_salesman_problem(G_BB, cycle=True, weight='weight'))
    
    # Ensure the tour starts and ends at the origin
    if tour[-1] != origin:
        tour.append(origin)
    if tour[0] != origin:
        tour.insert(0, origin)
        
    return tour

def analyze_tour(tour, cities):
    total_distance = 0
    max_distance = 0
    
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    
    # Return to the origin
    return_to_origin = euclidean_distance(cities[tour[-1]], cities[tour[0]])
    total_distance += return_to_origin
    max_distance = max(max_distance, return_to_rect_origin)
    
    return tour, total_distance, max_distance

# Coordinates of the cities (including the depot as city 0)
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Step 1: Create bottleneck-optimal biconnected subgraph
G_BB = create_biconnected_graph(cities)

# Step 2: Use Christofides algorithm to find an approximate optimal tour
origin = 0  # starting and ending at depot city
tour = approximate_tour(G_BB, origin)

# Analyze the tour to get requested metrics
analyzed_tour, total_cost, max_consecutive_distance = analyze_tour(tour, cities)

# Output the results
print("Tour:", analyzed_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_consecutive_distance, 2))