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

# Initialize the graph
G = nx.Graph()
number_of_cities = len(cities)

# Adding edges between every pair of cities with their distances
for i, j in combinations(range(number_of_cities), 2):
    dist = euclidean_distance(cities[i], cities[j])
    G.add_edge(i, j, weight=dist)

# Sort edges by weight
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['_weight'])

# Algorithm BB implementation

# Initialize biconnected subgraph storage
E_BB = []

# Use a Union-Find data structure to manage connected components
uf = nx.utils.UnionFind()

# Augmentation: Add edges by increasing weight and check biconnected
for u, v, data in sorted_edges:
    if uf[u] != uf[v]:
        uf.union(u, v)
        E_BB.append((u, v, data['weight']))

    # Form a subgraph from the selected edges
    G_BB = nx.Graph()
    G_BB.add_weighted_edges_from(E_BB)
    
    # Check biconnected condition: each component is biconnected and contains the depot (0)
    if nx.is_biconnected(G_BB):
        break

# Generate biconnected subgraph G_BB
G_BB = nx.Graph()
G_BB.add_weighted_edges_from(E_BB)

# Identify an approximate optimal tour using shortest paths between non-directly connected edges in BB
# making G_bb square
for u in G_BB.nodes:
    for v in G_BB.nodes:
        if u != v and not G_BB.has_edge(u, v):
            shortest_path_length = nx.dijkstra_path_length(G, u, v, weight='weight')
            G_BB.add_edge(u, v, weight=shortest_path_length)

# Find a Hamiltonian path starting and ending at depot in the square of the G_BB
tsp_tour = nx.approximation.traveling_salesman_problem(G_BB, cycle=True, weight='weight', nodes=[0])

# Calculate the travel cost and maximum distance between consecutive cities in the tour
total_travel_cost = sum(G_BB[u][v]['weight'] for u, v in zip(tour, tour[1:] + [tour[0]]))
max_distance_consecutive_cities = max(G_BB[u][v]['weight'] for u, v in zip(tour, tour[1:]))

print("Tour:", tsp_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_consecutive_cities)