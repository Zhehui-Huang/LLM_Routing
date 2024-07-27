import math
import networkx as nx
from itertools import permutations

# City coordinates
coordinates = [
    (54, 87),  # Depot city
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# Calculate Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create graph
def create_graph(coordinates):
    G = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i+1, n):
            dist = calculate_distance(coordinates[i], coordinates[j])
            G.add_edge(i, j, weight=dist)
    return G

# Calculate bottleneck for a route
def get_bottleneck(G, route):
    max_distance = float('-inf')
    total_distance = 0
    for i in range(len(route) - 1):
        weight = G[route[i]][route[i+1]]['weight']
        total_distance += weight
        if weight > max_distance:
            max_distance = weight
    return total_distance, max_distance

# Find approximate solution to BTSP
def btsp_approach(G):
    # Generate all possible tours starting and stopping at the depot
    all_possibilities = permutations(range(1, len(coordinates)))
    best_bottleneck = float('inf')
    best_tour = None
    best_cost = 0

    for perm in all_possibilities:
        tour = [0] + list(perm) + [0]
        total_cost, bottleneck = get_bottleneck(G, tour)
        if bottleneck < best_bottleneck or (bottleneck == best_bottleneck and total_cost < best_cost):
            best_bottleneck = bottleneck
            best_tour = tour
            best_cost = total_cost

    return best_tour, best_cost, best_bottleneck

# Create graph from coordinates
G = create_graph(coordinates)

# Solve BTSP
tour, total_cost, max_distance = btsp_approach(G)

# Results output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")