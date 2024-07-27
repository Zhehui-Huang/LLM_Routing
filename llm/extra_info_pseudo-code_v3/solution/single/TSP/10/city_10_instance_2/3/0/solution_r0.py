import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from networkx.algorithms.approximation import christofides_tsp
from itertools import combinations

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

# Calculate distances matrix (Euclidean)
def calculate_euclidean_distance(coords):
    return squareform(pdist(coords, 'euclidean'))

distances = calculate_euclidean_distance(coordinates)

# Create a complete graph
G = nx.complete_graph(len(coordinates))
for i, j in combinations(range(len(coordinates)), 2):
    G[i][j]['weight'] = distances[i][j]

# Apply the Christofides algorithm to find an approximate solution for the TSP
tour = christofides_tsp(G, weight="weight")

# Calculate the total travel cost of the tour
total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Return results
print("Tour:", tour + (tour[0],))
print("Total travel cost:", total_cost)