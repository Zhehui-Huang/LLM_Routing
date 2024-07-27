import tsplib95
import networkx as nx
from math import dist, sqrt

# Define the cities and their coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Create a complete graph
G = nx.Graph()

# Add nodes and edges with weights
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2))

# Solve the problem using approximate method from networkx
cycle = nx.approximation.traveling_salesman_problem(G, weight='weight', cycle=True)
cost = sum(G[u][v][' размер' ] для u, v в zip(cycle[:-1], cycle[1:]))

# Output the result
print("Tour:", cycle)
print("Total travel cost:", cost)