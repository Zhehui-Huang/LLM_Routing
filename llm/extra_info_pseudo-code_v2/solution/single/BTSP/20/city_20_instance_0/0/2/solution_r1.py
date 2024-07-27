import math
import numpy as np

# City coordinates
cities = [
    (8, 11),  # City 0 (Depot)
    (40, 6),  # City 1
    (95, 33), # City 2
    (80, 60), # City 3
    (25, 18), # City 4
    (67, 23), # City 5
    (97, 32), # City 6
    (25, 71), # City 7
    (61, 16), # City 8
    (27, 91), # City 9
    (91, 46), # City 10
    (40, 87), # City 11
    (20, 97), # City 12
    (61, 25), # City 13
    (5, 59),  # City 14
    (62, 88), # City 15
    (13, 43), # City 16
    (61, 28), # City 17
    (60, 63), # City 18
    (93, 15)  # City 19
]

def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Creating distance matrix
n = len(cities)
dist_matrix = [[calc_distance(cities[i], cities[j]) if i != j else float('inf') for j in range(n)] for i in range(n)]

# Minimum Spanning Tree with networkX
import networkx as nx

G = nx.complete_graph(n)
for i in range(n):
    for j in range(n):
        if i != j:
            G.add_edge(i, j, weight=dist_matrix[i][j])

# Finding MST using Kruskal's algorithm
mst = list(nx.minimum_spanning_edges(G, data=False))

# Function to find a tour from mst using preorder traversal of MST
def find_tour_mst(node, visited, mst_adj, tour):
    visited.add(node)
    tour.append(node)
    for neighbor in mst_adj[node]:
        if neighbor not in visited:
            find_tour_mst(neighbor, visited, mst_adj, tour)

# Create adjacency list from mst
mst_adj = {i: [] for i in range(n)}
for edge in mst:
    mst_adj[edge[0]].append(edge[1])
    mst_adj[edge[1]].append(edge[0])

# Find tour
tour = []
find_tour_mst(0, set(), mst_adj, tour)
tour.append(0)  # complete the cycle back to the start

# Calculating the tour's cost and maximum distance between any two consecutive cities
total_distance = 0
max_edge_length = 0
for i in range(1, len(tour)):
    edge_length = dist_matrix[tour[i-1]][tour[i]]
    total_distance += edge_length
    if edge_length > max_edge_length:
        max_edge_length = edge_length

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_edge_length}")