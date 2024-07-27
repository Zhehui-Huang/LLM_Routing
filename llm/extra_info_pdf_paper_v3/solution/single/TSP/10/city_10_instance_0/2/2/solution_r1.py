import math
import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from networkx.algorithms.approximation import traveling_salesman_problem

# City coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98),
    4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
    8: (61, 90), 9: (42, 49)
}

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph with cities as nodes and edges weighted by Euclidean distance
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Compute shortest path using Christofides algorithm provided by NetworkX
tsp_tour = traveling_salesman_problem(G, cycle=True, method='christofides')

# Calculate the cost of the tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(tsp_tour[:-1], tsp_tour[1:]))

# Ensure the tour starts and ends at the depot city (node 0)
if tsp_tour[0] != 0:
    idx = tsp_tour.index(0)
    tsp_tour = tsp_tour[idx:] + tsp_tour[:idx]
tsp_tour.append(0)  # Append the return to the starting city

# Output the results
print("Tour:", tsp_tour)
print("Total travel cost:", total_cost)