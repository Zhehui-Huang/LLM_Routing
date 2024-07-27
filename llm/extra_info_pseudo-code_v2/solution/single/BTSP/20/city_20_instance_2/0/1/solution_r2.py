import math
import networkx as nx

cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 91),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a complete weighted graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Utilize implementation of an optimal path finder from networkx (Christofides algorithm which approximates TSP)
from networkx.algorithms.approximation import traveling_salesman_problem
# Compute the approximate TSP path. This will be a Hamiltonian circuit.
tsp_path = traveling_salesman_problem(G, weight='weight', cycle=True)

# For the given task: we need the travel cost + max_distance between consecutive cities
total_cost = sum(G[tsp_path[i]][tsp_path[i+1]]['weight'] for i in range(len(tsp_path)-1))
max_distance = max(G[tsp_path[i]][tsp_path[i+1]]['weight'] for i in range(len(tsp_path)-1))

print(f"Tour: {tsp_path}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")