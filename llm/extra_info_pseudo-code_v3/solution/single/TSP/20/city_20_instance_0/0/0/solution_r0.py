import math
import networkx as nx

# Define the coordinates of the depot and other cities
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

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a complete graph with weighted edges between every pair of nodes
G = nx.Graph()
num_cities = len(coordinates)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        distance = euclidean or_distance(coordinates[i], coordinates[j])
        G.add_edge(i, j, weight=distance)