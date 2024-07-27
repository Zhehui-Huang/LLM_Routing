import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix
from networkx.algorithms import matching, tree

# Define the cities and their coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Compute the distance matrix
coords = np.array(list(cities.values()))
dist_matrix = distance_matrix(coords, coords)

# Create a complete graph
G = nx.complete_graph(len(cities))

# Set the weights of the graph
for i in range(len(cities)):
    for j in range(len(cities)):
        G[i][j]['weight'] = dist_matrix[i][j]