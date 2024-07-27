import math
import networkx as nx
from itertools import combinations

# Coordinates of the cities
cities = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28),
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(ci, cj):
    return math.sqrt((ci[0] - cj[0])**2 + (ci[1] - cj[1])**2)

# Initialize the graph G
G = nx.Graph()
number_of_cities = len(cities)

# Adding edges with Euclidean distances
for i, j in combinations(range(number_of_cities), 2):
    dist = euclidean_distance(cities[i], cities[j])
    G.add_edge(i, j, weight=dist)

# Algorithm BB - Bottleneck-optimal Biconnected Subgraph
sorted_edges = sorted(G.edges(data='weight'), key=lambda x: x[2])
uf = nx.utils.UnionFind()

# Initialize empty graph for E_BB
G_BB = nx.Graph()

# Include edges causing the graph to be biconnected
for u, v, weight in sorted_edges:
    G_BB.add_edge(u, v, weight=weight)
    if uf[u] != uf[v]:
        uf.union(u, v)
    if nx.is_biconnected(G_BB):
        break

# Tour Identification in squared subgraph of G_BB
# Arguably this part could be much different, here we'll use approximation directly from G
tsp_tour = nx.approximation.traveling_salesman_problem(G, cycle=True, weight='weight', nodes=[0])
# Other example uses the square of the biconnected subgraph, which can be created and used in a similar way.

# Calculate the travel cost and maximum distance between consecutive cities in the tour
total_travel_cost = sum(G[tsp_tour[i]][tsp_tour[i+1]]['weight'] for i in range(len(tsp_tour)-1))
max_distance_consecutive_cities = max(G[tsp_tour[i]][tsp_tour[i+1]]['weight'] for i in range(len(tsp_tour)-1))

# Provide results
print("Tour:", tsp_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_consecutive_cities)