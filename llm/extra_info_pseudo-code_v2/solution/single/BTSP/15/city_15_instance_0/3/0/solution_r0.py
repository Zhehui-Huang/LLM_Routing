from math import sqrt
import networkx as nx

# Define cities and their coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Step 0: Calculate edges and weights
edges = {}
for i in cities:
    for j in cities:
        if i != j:
            edges[(i, j)] = euclidean_distance(cities[i], cities[j])

# Sorted list of edges based on distance
sorted_edges = sorted(edges.items(), key=lambda item: item[1])

# Step 1: Generate a bottleneck-optimal biconnected subgraph
G = nx.Graph()
for edge, weight in sorted_edges:
    G.add_edge(*edge, weight=weight)
    if nx.is_biconnected(G):
        break

# Check biconnectedness correctness and compute max edge weight in current subgraph
if nx.is_biconnected(G):
    bottleneck_value = max([G[u][v]['weight'] for u, v in G.edges()])
else:
    print("Failed to find biconnected graph")
    exit()

# Step 2: Compute an approximate optimal tour as a Hamiltonian cycle
G_square = nx.power(G, 2)  # Create G^2
cycle = nx.approximation.traveling_salesman_problem(G_square, cycle=True, weight='weight')

# Calculate the costs
cycle_edges = zip(cycle, cycle[1:] + [cycle[0]])
max_edge_length = 0
total_cost = 0
for u, v in cycle_edges:
    distance = edges[(u, v)] if (u, v) in edges else edges[(v, u)]
    total_cost += distance
    max_edge_length = max(max_edge_length, distance)

# Output
print(f"Tour: {cycle + [cycle[0]]}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_edge_length}")