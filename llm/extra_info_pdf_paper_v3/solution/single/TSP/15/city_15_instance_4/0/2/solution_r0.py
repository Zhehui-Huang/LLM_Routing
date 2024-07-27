import math
import networkx as nx
from scipy.spatial import distance
from itertools import combinations

# Cities coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate Euclidean distances
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Complete Graph
G = nx.Graph()

# Adding edges
for c1, c2 in combinations(cities.keys(), 2):
    G.add_edge(c1, c2, weight=calc_distance(c1, c2))

# Minimum Spanning Tree
MST = nx.minimum_spanning_tree(G)

# Find vertices of odd degree
odd_degree_nodes = [v for v, degree in MST.degree() if degree % 2 == 1]

# Minimum Weight Perfect Matching on vertices with odd degree
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.max_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add Minimum Weight Perfect Matching edges to MST
MST_matching = MST.copy()
for edge in min_weight_matched:
    if MST_matching.has_edge(*edge):
        MST_matching[edge[0]][edge[1]]['weight'] = 0  # This should not happen according to the algorithm.
    else:
        MST_matching.add_edge(edge[0], edge[1], weight=calc_distance(*edge))

# Find Eulerian Circuit (which should exist because all nodes have even degree now)
eulerian_circuit = list(nx.eulerian_circuit(MST_matching, source=0))

# Convert the Eulerian circuit to Hamiltonian path
visited = set()
path = []

for u, v in eulerian_circuit:
    if u not in visited:
        path.append(u)
        visited.add(u)
    if v not in visited:
        path.append(v)
        visited.add(v)

# Include final return to the depot
path.append(0)

# Calculate total travel cost
total_cost = sum(calc_distance(path[i], path[i+1]) for i in range(len(path)-1))

print(f'Tour: {path}')
print(f'Total travel cost: {total_cost}')