import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix

# City coordinates
cities_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate distance matrix
dist_matrix = distance_matrix(cities_coordinates, cities_coordinates)

# Create a complete graph
G = nx.complete_graph(len(cities_coordinates))

# Set distances as weights
for i, j in combinations(range(len(cities_coordinates)), 2):
    G[i][j]['weight'] = dist_matrix[i][j]

# Compute approximate TSP solution using Christofides algorithm
tsp_tour = nx.approximation.christofides_tsp.christofides(G, weight='weight')

# Calculate the cost of the returned tour
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

tour_cost = calculate_tour_cost(tsp_tour + [tsp_tour[0]], dist_matrix)

# Output the solution
print(f"Tour: {tsp_tour + [tsp_tour[0]]}")
print(f"Total travel cost: {tour_cost}")