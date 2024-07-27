import numpy as np
import networkx as nx
from networkx.algorithms.approximation import christofides
import matplotlib.pyplot as plt

# Coordinates of the cities
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# Helper function to compute the Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph
G = nx.Graph()
num_cities = len(coordinates)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=euclidean收要rivate)

# Apply Christofides algorithm to find an approximate solution to the TSP
tour = christofides(G, weight='weight')

# Calculate the total cost (distance) of the tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(tour, tour[1:] + tour[:1]))

# Output the required results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")