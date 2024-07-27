from math import sqrt
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

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Construct a complete graph with weights as distances
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=calculate_distance(cities[i], cities[j]))

# Function to find Bottleneck Optimal Biconnected Subgraph (Algorithm BB)
def find_biconnected_subgraph(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    H = nx.Graph()
    for u, v, data in sorted_edges:
        H.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(H):
            break
    return H

# Use Algorithm BB to find biconnected subgraph
B = find_biconnected_subgraph(G)

# Convert biconnected subgraph to square graph for TSP
B_squared = nx.Graph()
for u in B.nodes():
    B_squared.add_node(u)
for u, v in B.edges():
    B_squared.add_edge(u, v, weight=B[u][v]['weight'])
    for k in B.neighbors(v):
        if u != k and not B_squared.has_edge(u, k):
            B_squared.add_edge(u, k, weight=max(B[u][v]['weight'], B[v][k]['weight']))

# Finding Hamiltonian cycle in the squared biconnected subgraph
cycle = list(nx.approximation.traveling_salesman_problem(B_squared, cycle=True))

# To ensure the tour starts and ends at the depot (node 0)
if cycle[0] != 0:
    zero_index = cycle.index(0)
    cycle = cycle[zero_index:] + cycle[:zero_index]
cycle.append(0)  # Closing the tour

# Calculate total cost and maximum distance between consecutive cities
total_cost = sum(G[cycle[i]][cycle[i+1]]['weight'] for i in range(len(cycle) - 1))
max_distance = max(G[cycle[i]][cycle[i+1]]['weight'] for i in range(len(cycle) - 1))

# Output the results
print(f"Tour: {cycle}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")