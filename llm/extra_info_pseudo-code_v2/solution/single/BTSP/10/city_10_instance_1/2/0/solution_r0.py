from math import sqrt
from itertools import combinations
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

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Construct a complete graph with weights as distances
G = nx.Graph()
for (i, coord_i), (j, coord_j) in combinations(cities.items(), 2):
    G.add_edge(i, j, weight=calculate_distance(coord_i, coord_j))

# Find Bottleneck Optimal Biconnected Subgraph using Kruskal's as a base (Algorithm BB)
def find_biconnected_subgraph(G):
    MST = list(nx.minimum_spanning_edges(G, data=True))
    H = nx.Graph()
    H.add_edges_from(MST)
    edge_weights = sorted((data['weight'], u, v) for u, v, data in G.edges(data=True))
    
    for weight, u, v in edge_weights:
        if not nx.has_path(H, u, v) or not nx.is_biconnected(H):
            H.add_edge(u, v, weight=weight)
        if nx.is_biconnected(H):
            break
    
    return H

# Apply Algorithm BB
B = find_biconnected_subgraph(G)

# Define a suitable Hamiltonian cycle (from the full graph, simplistically the MST + edges)
# For simplicity, we use the minimum weight Hamiltonian cycle (Traveling Salesman)
cycle = list(nx.approximation.traveling_salesman_problem(B, cycle=True))
cycle.append(cycle[0])  # to make the cycle complete by returning to the start

# Calculations to output
total_cost = sum(G[cycle[i]][cycle[i+1]]['weight'] for i in range(len(cycle) - 1))
max_distance = max(G[cycle[i]][cycle[i+1]]['f(weight)'] for i in range(len(cycle) - 1))

# Output the results
print(f"Tour: {cycle}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")