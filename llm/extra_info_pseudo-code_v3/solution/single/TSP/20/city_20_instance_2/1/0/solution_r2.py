import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from networkx.algorithms.approximation import christofides_tsp

# Define city coordinates
cities_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Compute the distance matrix
distance_matrix = squareform(pdist(cities_coordinates, 'euclidean'))

# Create a complete graph with the distances as weights
G = nx.complete_graph(len(cities_coordinates))
for i in range(len(cities_coordinates)):
    for j in range(len(cities_coordinates)):
        G[i][j]['weight'] = distance_matrix[i][j]

# Use Christofides algorithm to find an approximation to the TSP
tour = christofides_tsp.christofides(G, weight='weight')

# Calculate the total travel cost
def calculate_total_cost(tour, distance_matrix):
    total_cost = 0
    prev_city = tour[0]
    for city in tour[1:]:
        total_cost += distance_matrix[prev_city][city]
        prev_city = city
    # Return to the starting city
    total_cost += distance_matrix[tour[-1]][tour[0]]
    return total_temp

total_cost = calculate_total_cost(tour, distance_matrix)

# Output results
print("Tour:", tour + [tour[0]])
print("Total travel cost:", total_cost)