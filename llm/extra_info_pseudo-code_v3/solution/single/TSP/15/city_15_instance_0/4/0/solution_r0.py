import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms import matching
from networkx.algorithms.approximation import christofides

# Define coordinates of cities including the depot
city_coords = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39),   # City 14
]

# Create distance matrix using Euclidean distance
dist_matrix = distance_matrix(city_coords, city_coords)
num_cities = len(city_coords)

# Create a complete graph from the distance matrix
G = nx.complete_graph(num_cities)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G[i][j]['weight'] = dist_matrix[i][j]

# Compute the tour using Christofides' algorithm
tour = christofides(G, weight='weight')

# Calculate the total travel cost of the tour
total_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")