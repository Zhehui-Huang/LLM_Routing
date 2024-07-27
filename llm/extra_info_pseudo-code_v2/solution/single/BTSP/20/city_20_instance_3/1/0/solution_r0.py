import math
from itertools import combinations
import networkx as nx

# City coordinates given in the problem statement
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}

# Utility function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Creating a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Algorithm BB to find Bottleneck-Optimal Biconnected Subgraph
def algorithm_bb(G):
    edges_sorted_by_weight = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = nx.Graph()
    E_BB.add_nodes_from(G.nodes())
    
    for u, v, data in edges_sorted_by_weight:
        E_BB.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(E_BB):
            return E_BB
    
    return E_BB  # in case all edges are needed, though unlikely

# Step 1: Find the bottleneck-optimal biconnected subgraph
E_BB = algorithm_bb(G)

# Insert extra edges to form the square of graph E_BB if necessary
E_BB2 = E_BB.copy()
for u in E_BB.nodes():
    neighbors = list(E_BB.neighbors(u))
    for i, j in combinations(neighbors, 2):
        if not E_BB2.has_edge(i, j):
            weight = max(E_BB[u][i]['weight'], E_BB[u][j]['weight'])
            E_BB2.add_edge(i, j, weight=weight)

# Step 2: Identify an approximate optimal tour using a Hamiltonian approximation method
tour = list(nx.approximation.traveling_salesman_problem(E_BB2, cycle=True, weight='weight'))
tour.append(tour[0])  # to return to the starting city

# Calculate total travel cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(len(tour)-1):
    dist = distance(tour[i], tour[i+1])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")