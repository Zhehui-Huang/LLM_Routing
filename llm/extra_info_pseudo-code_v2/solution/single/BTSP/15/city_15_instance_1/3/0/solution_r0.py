import numpy as np
import itertools
import networkx as nx

# Coordinates of the cities
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Number of cities including the depot
n = len(cities)

# Create a full graph with n nodes
G = nx.complete_graph(n)

# Assign weights to the edges based on Euclidena distances
for i in range(n):
    for j in range(i + 1, n):
        G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])

# Sorting edges by weight
sorted_edges = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])

# Step 1: Bottleneck-optimal Biconnected Subgraph with Algorithm BB
E_BB = []
BB_graph = nx.Graph()

for i, j, data in sorted_edges:
    BB_graph.add_edge(i, j, weight=data['weight'])
    if not nx.is_biconnected(BB_graph):
        BB_graph.remove_edge(i, j)
    if nx.is_biconnected(BB_graph):
        break

# Step 2: Find a Hamiltonian cycle in the squared graph of the BB subgraph
# Get the square of the graph
BB_squared = nx.power(BB_graph, 2)

# Use an approximate method to find a Hamiltonian cycle, such as Christofides' algorithm
# However, direct Hamiltonian path finding is NP-Hard, we use approximation

# We adapt the traveling salesperson approximation for now
cycle = nx.approximation.traveling_salesman_problem(BB_squared, cycle=True)

# Output Results
travel_costs = [G[cycle[i]][cycle[i+1]]['weight'] for i in range(len(cycle)-1)]
total_travel_cost = sum(travel_costs)
max_travel_cost = max(travel_costs)

print("Tour:", cycle)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_travel_cost)