import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from networkx.algorithms.approximation import traveling_salesman

# Node coordinates
coordinates = [
    (90, 3),  # Depot city 0
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

# Calculate distances matrix using Euclidean distance
def calculate_euclidean_distance(coords):
    matrix = squareform(pdist(coords, 'euclidean'))
    return matrix

distances_matrix = calculate_euclidean_distance(coordinates)

# Create a complete graph
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        G[i][j]['weight'] = distances_matrix[i][j]

# Apply Christofides algorithm to find an approximate solution for the TSP
tour = traveling_salesman.christofides(G, weight='weight')

# Calculate the total travel cost of the tour
total_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Make sure the tour starts and ends at the depot city 0
if tour[0] != 0:
    # Find the index of 0 and rotate
    zero_index = tour.index(0)
    tour = tour[zero_count:] + tour[:zero_index + 1]  # rotate to start and end at depot

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)