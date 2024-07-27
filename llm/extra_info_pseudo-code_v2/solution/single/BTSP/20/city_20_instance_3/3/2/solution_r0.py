import math
from itertools import combinations
from collections import defaultdict
import networkx as nx

# Distance calculator using Euclidean distance
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Define the cities and their locations
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Step 0: Initialize graph G and sort edges by weights
G = nx.Graph()
for (i, coord_i), (j, coord_j) in combinations(cities.items(), 2):
    distance = calculate_distance(coord_i, coord_j)
    G.add_edge(i, j, weight=distance)

edges_sorted_by_weights = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Algorithm BB to obtain a biconnected subgraph with minimal maximal edge weight
E_BB = nx.Graph()
E_BB.add_nodes_from(G.nodes())

for edge in edges_sorted_by_weights:
    E_BB.add_edge(*edge[:2], weight=edge[2]['weight'])
    if nx.is_biconnected(E_BB):
        break

# Step 2: Identify a Hamiltonian cycle in the biconnected subgraph
# We revert to networkx's approximation method for a Hamiltonian circuit
cycle = nx.approximation.traveling_salesman_problem(E_BB, cycle=True, method='greedy')
cycle.append(cycle[0])  # To make it a complete tour starting and ending at the same city

# Compute the travel cost and the maximum distance
total_travel_cost = sum(G[u][v]['weight'] for u, v in zip(cycle[:-1], cycle[1:]))
max_distance = max(G[u][v]['weight'] for u, v in zip(cycle[:-1], cycle[1:]))

# Output the result
print("Tour:", cycle)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance)