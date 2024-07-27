import math
import networkx as nx
from itertools import combinations

# Locations of the cities, including the depot
locations = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
]

# Euclidean distance calculator function
def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

# Create a complete graph with the Euclidean distances as edges weights
G = nx.complete_graph(len(locations))
for (u, v) in G.edges():
    G[u][v]['weight'] = euclidean_distance(locations[u], locations[v])

# Implement the BB Algorithm to create a bottleneck-optimal biconnected subgraph
edges_sorted_by_weight = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
subgraph = nx.Graph()

for edge in edges_sorted_by_weight:
    subgraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    if nx.is_biconnected(subgraph):
        break

# Identify an approximate optimal tour for BTSP in the biconnected subgraph
# The square of the subgraph typically relaxes adjacency restrictions useful in finding a Hamiltonian cycle
subgraph_square = nx.power(subgraph, 2)
tsp_tour = nx.approximation.traveling_salesman_problem(subgraph_square, cycle=True)

# Calculate the total cost and maximum distance between consecutive cities in the tour
total_travel_cost = sum(subgraph_square[u][v]['weight'] for u, v in zip(tsp_tour[:-1], tsp_tour[1:]))
max_consecutive_distance = max(subgraph_square[u][v]['weight'] for u, v in zip(tsp_tour[:-1], tsp_tour[1:]))

# Making sure the tour starts and ends at the depot
if tsp_tour[0] != 0:
    zero_index = tsp_tour.index(0)
    tsp_tour = tsp_tour[zero_index:] + tsp_tour[:zero_index]
tsp_tour.append(0)

print("Tour:", tsp_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_distance)