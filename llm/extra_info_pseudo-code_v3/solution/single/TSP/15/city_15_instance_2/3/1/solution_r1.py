import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations
from networkx.algorithms.approximation import christofides

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

n = len(cities)
coords = np.array(list(cities.values()))
dist_matrix = squareform(pdist(coords, metric='euclidean'))

# Create a complete graph 
G = nx.complete_graph(n)
for i in range(n):
    for j in range(n):
        if i != j:
            G.edges[i, j]['weight'] = dist_matrix[i][j]

# Calculate the Christofides' TSP approximation solution        
path = christofides(G)

# Computing total travel cost
total_cost = sum(dist_matrix[path[i], path[i+1]] for i in range(len(path)-1))
total_cost += dist_matrix[path[-1], path[0]]  # returning to start

# Output the results
print(f"Tour: {path}")
print(f"Total travel cost: {total_cost:.2f}")