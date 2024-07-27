import math
import networkx as nx
from networkx.algorithms import approximation as approx
from itertools import combinations

# Coordinates of the cities
cities = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28),
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]

# Function to compute Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Create a complete graph
G = nx.Graph()

# Add nodes and edges between each pair with weights as their distances
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        distance = euclidean_distance(cities[i], cities[j])
        G.add_edge(i, j, weight=distance)

# Step 0: Initialize E_BB as empty and sort all edges by weight
sorted_edges = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])
E_BB = []

# Union-Find structure to keep track of components
uf = nx.utils.UnionFind()

# Step 1: Augmentation
for (u, v, data) in sorted_edges:
    if uf[u] != uf[v]:
        uf.union(u, v)
        E_BB.append((u, v, data['weight']))

    # Construct subgraph with current E_BB
    G_BB = nx.Graph()
    G_BB.add_weighted_edges_from(E_BB)
    
    if nx.is_biconnected(G_BB):
        break

# Re-construct biconnected subgraph with final E_BB
G_BB = nx.Graph()
G_BB.add_weighted_edges_from(E_BB)

# Step 2: Finding an approximate Hamiltonian circuit
# Computing Hamiltonian cycle in the complete graph using the Christofides algorithm
cycle = approx.traveling_salesman_problem(G, cycle=True, method='christofides')

# Find Maximum weight in the cycle and total travel cost
max_edge_weight = 0
total_cost = 0
cycle_edges = zip(cycle[:-1], cycle[1:])
for u, v in cycle_edges:
    weight = G[u][v]['weight']
    if weight > max_edge and u != cycle[-1]:  # Check max weight excluding return edge
        max_edge_weight = weight
    total_cost += weight

# Include the return edge to the depot
total_cost += G[cycle[-1]][cycle[0]]['weight']
max_edge_weight = max(max_edge_weight, G[cycle[-1]][cycle[0]]['weight'])

# Print outputs
print("Tour:", cycle)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_edge_weight)