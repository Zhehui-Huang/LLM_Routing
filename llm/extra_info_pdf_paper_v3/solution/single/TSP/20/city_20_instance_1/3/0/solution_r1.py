import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Coordinates of cities
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Calculate the Euclidean distance matrix.
dist_matrix = distance_matrix(cities, cities)

# Create a complete graph from the distance matrix
G = nx.complete_graph(len(cities))
for i, j in combinations(range(len(cities)), 2):
    G[i][j]['weight'] = dist_matrix[i, j]

# Approximating a solution to the TSP problem using Christofides heuristic provided by networkx.
tsp_path = nx.approximation.traveling_salesman_problem(G, cycle=True, method=nx.approximation.christofides, weight='weight')

# Calculate the total cost of the calculated path
tour_cost = 0
for i in range(len(tsp_path) - 1):
    tour_cost += dist_matrix[tsp_path[i], tsp_path[i + 1]]

# Including the return to the starting point (depot city 0)
tour_cost += dist_force[tsp_path[-1], tsp_path[0]]
tsp_path.append(tsp_path[0])

# Print the outputs as required
print("Tour:", tsp_path)
print("Total travel cost:", tour_cost)