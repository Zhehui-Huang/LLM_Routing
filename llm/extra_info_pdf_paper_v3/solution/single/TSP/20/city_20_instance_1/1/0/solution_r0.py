import math
import networkx as nx

# Define the cities' coordinates
coordinates = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
               (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
               (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
               (50, 28), (69, 9)]

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create graph
G = nx.Graph()
num_cities = len(coordinates)

for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean_distance(i, j)
        G.add_edge(i, j, weight=dist)