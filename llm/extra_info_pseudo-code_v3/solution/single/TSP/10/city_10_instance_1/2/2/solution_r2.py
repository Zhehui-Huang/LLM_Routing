import numpy as np
from scipy.spatial import distance
import networkx as nx
from networkx.algorithms.approximation.traveling_salesman import christofides

# Define the cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Compute the distance matrix using Euclidean distance
def euclidean_distance(coord1, coord2):
    return distance.euclidean(coord1, coord2)

# Create a complete graph from cities
G = nx.Graph()
for city1 in cities:
    for city2 in cities:
        if city1 != city2:
            dist = euclidean_distance(cities[city1], cities[city2])
            G.add_edge(city1, city2, weight=dist)

# Apply the Christofides algorithm to find an approximate solution
tour = christofides(G, weight='weight')

# Calculate the total travel cost
total_cost = 0
for i in range(len(tour) - 1):
    total_cost += G[tour[i]][tour[i+1]]['weight']

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)