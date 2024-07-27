import math
import networkx as nx

# Function to calculate the Euclidean distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Coordinates for 20 cities
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}

# Create the complete graph with weighted edges between all city pairs
G = nx.Graph()
for city1 in cities:
    for city16 in cities:
        if city1 != city16:
            dist = calculate_distance(cities[city1], cities[city16])
            G.add_edge(city1, city16, weight=dist)

# Sort edges by weight
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Create a subgraph and add edges until the subgraph is biconnected
H = nx.Graph()
H.add_nodes_from(G.nodes())
for edge in sorted_edges:
    H.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    if nx.is_biconnected(H):
        break

# Find a Hamiltonian cycle in the squared biconnected subgraph
H_squared = nx.Graph()
H_squared.add_nodes_from(H.nodes())
for u in H:
    for v in nx.single_source_shortest_path_length(H, u, cutoff=2):
        if u != v:
            H_squared.add_edge(u, v, weight=G[u][v]['weight'] if v in G[u] else float('inf'))

cycle = nx.approximation.traveling_salesman_problem(H_squared, cycle=True, weight='weight')
cycle.append(cycle[0])  # make it a round trip

# Calculate the tour cost
total_cost = sum(G[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle)-1))
max_edge_cost = max(G[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle)-1))

# Print the results
print("Tour:", cycle)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_edge_cost)