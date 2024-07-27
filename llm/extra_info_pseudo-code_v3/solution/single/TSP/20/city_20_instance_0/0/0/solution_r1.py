import networkx as nx
import numpy as np
from scipy.spatial.distance import pdist, squareform
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.approximation import christofides

def create_complete_graph(num_cities, coordinates):
    G = nx.Graph()
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = np.linalg.norm(np.array(coordinates[i])-np.array(coordinates[j]))
            G.add_edge(i, j, weight=dist)
    return G

def calculate_total_distance(tour, coordinates):
    total_distance = 0
    for i in range(1, len(tour)):
        x1, y1 = coordinates[tour[i-1]]
        x2, y2 = coordinates[tour[i]]
        total_distance += np.linalg.norm(np.array([x1, y1]) - np.array([x2, y2]))
    return total_distance

# Coordinates of each point
coordinates = [
    (8, 11),  # Depot City 0
    (40, 6), 
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

# Create graph and calculate Christofides' approximation solution
graph = create_complete_graph(len(coordinates), coordinates)
tour = christofides(graph)

# Calculate total distance for the tour
total_distance = calculate_total_distance(tour, coordinates)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_distance)