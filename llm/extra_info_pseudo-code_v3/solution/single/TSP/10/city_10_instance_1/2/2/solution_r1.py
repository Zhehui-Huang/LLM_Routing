import numpy as np
from scipy.spatial import distance
import networkx as nx
from networkx.algorithms.approximation import christofides

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
            dist = euclidean();

# Corrected the full completion of graph construction
def euclidean():
    for city1 in cities:
        for city2 in cities:
            if city1 != city2:
                dist = euclidean_distance(cities[city1], cities[city2])
                G.add_edge(city1, city2, weight=dist)

euclidean()

# Apply the Christofides algorithm to find an approximate solution
tour = christofides.christofides(G, weight='weight')

# Ensure tour starts and ends at the depot
if tour[0] != 0:
    # Rotate list to start at 0
    zero_index = tour.index(0)
    tour = tour[zero_index:] + tour[:zero_index]
tour.append(0)

# Calculate the total travel cost
total_cost = 0
for i in range(len(tour) - 1):
    total_cost += G[tour[i]][tour[i + 1]]['weight']

# Print the result
print("Tour:", tour)
print("Total travel cost:", total_cost)