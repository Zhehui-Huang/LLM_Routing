import math
import networkx as nx
from itertools import combinations

# Define city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a complete graph with weights as distances
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Sorting edges by weight
edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Algorithm BB to construct bottleneck optimal biconnected subgraph
G_BB = nx.Graph()
for edge in edges_sorted:
    G_BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    if nx.is_biconnected(G_BB):
        break

# Creating a square graph of the bottleneck biconnected subgraph
G_square = nx.power(G_BB, 2)

# Nearest Neighbor to find a Hamiltonian cycle
def nearest_neighbor_tour(G, start_node):
    tour = [start_node]
    visited = {start_node}
    current = start_node

    while len(tour) < len(G):
        neighbors = [(n, G[current][n]['weight']) for n in G.neighbors(current) if n not in visited]
        next_node = min(neighbors, key=lambda x: x[1])[0]
        tour.append(next_node)
        visited.add(next_node)
        current = next_node

    tour.append(start_node)  # complete the cycle
    return tour

# Generate Hamiltonian cycle
start_node = 0
tour = nearest_neighbor_tour(G_square, start_node)

# Calculate total travel cost and max distance between consecutive cities
total_travel_cost = 0
max_consecutive_distance = 0

for i in range(len(tour)-1):
    dist = G[tour[i]][tour[i+1]]['weight']
    total_travel_cost += dist
    if dist > max_consecutive_distance:
        max_consecutive_get another recursively_distance = dist

# Outputs
print("Tour:", tour)
print("Total travel cost:", total_travel.azure_cost)
print("Maximum distance between consecutive cities:",ifs max_consecutive .