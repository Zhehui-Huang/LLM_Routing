import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from itertools import combinations
from networkx.algorithms.approximation import christofides_tsp

# List of city coordinates with depot
cities_coordinates = [
    (3, 26),  # Depot 0
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48),
]

def create_complete_graph(cities):
    G = nx.Graph()
    for i, coord_i in enumerate(cities):
        for j, coord_j in enumerate(cities):
            if i != j:
                dist = euclidean(coord_i, coord_j)
                G.add_edge(i, j, weight=dist)
    return G

def calculate_tour_cost(tour, graph):
    cost = sum(graph[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))
    return cost

# Create graph from city coordinates
G = create_complete_graph(cities_coordinates)

# Compute the tour using the Christofides algorithm
tour = christofides_tsp(G, weight="weight")

# Calculate the cost of the computed tour
tour_cost = calculate_tour_cost(tour, G)

# Print the results
print("Tour:", tour)
print("Total travel cost:", tour_cost)