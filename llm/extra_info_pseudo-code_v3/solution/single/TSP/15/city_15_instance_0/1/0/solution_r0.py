import math
import networkx as nx
from itertools import combinations
from networkx.algorithms.approximation import christofides

# Cities coordinates with city index as key
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    
# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            dist = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)

# Applying Christofides algorithm to find TSP tour
tour = christofides(G)