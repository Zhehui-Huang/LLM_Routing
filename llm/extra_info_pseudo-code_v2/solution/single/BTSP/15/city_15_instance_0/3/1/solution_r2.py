import math
import networkx as nx
from itertools import permutations

# Define the coordinates for each city including the depot
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23),
    (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a function to compute the minimum spanning tree (MST) and convert to biconnected
def generate_biconnected_graph(cities):
    num_cities = len(cities)
    graph = nx.Graph()

    # Add all nodes in the graph
    graph.add_nodes_from(range(num_cities))

    # Sort edges by distance and add to create MST
    edges = [(i, j, euclidean_distance(cities[i], cities[j])) for i in range(num_cities) for j in range(i + 1, num_cities)]
    edges.sort(key=lambda x: x[2])  # Sort edges based on distance

    # Adding edges one by one checking for biconnectivity
    for u, v, weight in edges:
        graph.add_edge(u, v, weight=weight)
        if nx.is_biconnected(graph):
            break

    return graph

# Heuristic to find a tour that minimizes maximum leg distance
def find_min_max_distance_tour(graph, cities):
    best_tour = None
    min_max_distance = float('inf')

    # Generate all permutations of city indices, ensuring depot, city[0], is the start and end
    for perm in permutations(range(1, len(cities))):
        tour = (0,) + perm + (0,)

        # Check max distance in the current tour
        max_dist = max(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_tour = tour

    total_distance = sum(euclidean_distance(cities[best_tour[i]], cities[best_tour[i + 1]]) for i in range(len(best_tour) - 1))
    return best_tour, total_distance, min_max_distance

# Generate the biconnected graph
biconnected_graph = generate_biconnected_graph(cities)

# Find the optimal tour using a heuristic from this graph
tour, total_distance, max_distance = find_min_max_distance_tour(biconnected_graph, cities)

# Output the results with the tour, total distance traveled, and max leg distance
print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)