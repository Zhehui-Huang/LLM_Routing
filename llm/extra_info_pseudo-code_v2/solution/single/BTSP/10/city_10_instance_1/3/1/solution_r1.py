from itertools import combinations
import numpy as np
import networkx as nx

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a complete graph
G = nx.complete_graph(len(cities))
for i, j in combinations(cities, 2):
    G[i][j]['weight'] = euclidean_distance(countries[i], countries[j])

# Create edges list and sort by weight
edges = list(G.edges(data=True))
edges.sort(key=lambda x: x[2]['weight'])

# Function to check if graph is biconnected
def is_biconnected(G):
    return nx.is_biconnected(G)

# Step 1: Algorithm BB
E_BB = set()
G_BB = nx.Graph()

for edge in edges:
    G_BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    if is_biconnected(G_BB):
        break

# Step 2: Tour Identification
# Creating G^2 graph
G_squared = nx.Graph()
for node in G_BB.nodes():
    for neighbor in nx.single_source_shortest_path(G_BB, node, cutoff=2):
        if neighbor != node:
            G_squared.add_edge(node, neighbor, weight=G_BB[node][neighbor]['weight'])

# Find Hamiltonian cycle - approximation using TSP
cycle = nx.approximation.traveling_salesman_problem(G_squared, cycle=True, weight='weight')

# Evaluate the solution
total_cost = sum(G[u][v]['weight'] for u, v in zip(cycle[:-1], cycle[1:]) if (u, v) in G.edges)
max_distance = max(G[u][v]['weight'] for u, v in zip(cycle[:-1], cycle[1:]) if (u, v) in G.edges)

# Output sections
print(f"Tour: {cycle}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")