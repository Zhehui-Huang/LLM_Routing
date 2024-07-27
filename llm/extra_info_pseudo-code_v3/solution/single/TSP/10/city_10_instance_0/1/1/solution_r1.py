import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix
from networkx.algorithms.approximation import christofides

# List of city coordinates with Depot city included
coordinates = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Creating a Euclidean Distance Matrix
city_dist_matrix = distance_matrix(coordinates, coordinates)

# Creating a graph and adding edges along with their weights
G = nx.Graph()
num_cities = len(coordinates)

for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=city_dist_matrix[i][j])

# Using the Christofides algorithm to get an approximate solution
tsp_tour = christofides(G, weight="weight")

# Calculate the total cost of the tour
total_cost = sum(city_dist_matrix[tsp_tour[i], tsp_tour[i + 1]] for i in range(len(tsp_tour) - 1))  # Correct in the loop
total_cost += city_dist_matrix[tsp_tour[-1], tsp_tour[0]]  # Closing the tour by returning to the depot city

print(f"Tour: {tsp_tour}")
print(f"Total travel cost: {total_cost:.2f}")