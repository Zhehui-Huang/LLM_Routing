import math
from itertools import combinations
import networkx as nx

# Coordinates of cities (including the depot)
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Helper function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Step 0: Initialization - Calculate distances and sort edges
edges = []
for (i, j) in combinations(cities.keys(), 2):
    dist = euclidean_distance(cities[i], cities[j])
    edges.append((i, j, dist))
edges.sort(key=lambda x: x[2])  # sort by distance

# Step 1: Generate a bottleneck optimal biconnected subgraph using edges
G = nx.Graph()
nodes = cities.keys()
G.add_nodes_from(nodes)

for (i, j, d) in edges:
    G.add_edge(i, j, weight=d)
    # Check if the graph is biconnected
    if nx.is_biconnected(G):
        break

# Step 2: Find a tour in the squared graph of the biconnected subgraph
# Generate the square of the graph
G_squared = nx.Graph()
for (u, v, d) in G.edges(data=True):
    G_squared.add_edge(u, v, weight=d['weight'])
    for k in G.adj[u]:
        if k != v:
            distance = euclidean_distance(cities[v], cities[k])
            G_squared.add_edge(v, k, weight=distance)

# Find an approximate Hamiltonian cycle (tour)
cycle = nx.approximation.traveling_salesman_problem(G_squared, weight='weight', cycle=True)

# Generate tour outputs
total_cost = sum(euclidean_distance(cities[cycle[i]], cities[cycle[i + 1]]) for i in range(len(cycle) - 1))
max_distance = max(euclidean_distance(cities[cycle[i]], cities[cycle[i + 1]]) for i in range(len(cycle) - 1))

print("Tour:", cycle)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))