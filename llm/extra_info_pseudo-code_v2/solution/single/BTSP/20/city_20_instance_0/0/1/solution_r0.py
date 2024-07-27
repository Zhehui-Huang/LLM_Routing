import math
import networkx as nx

# City coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create a complete graph
G = nx.complete_graph(len(cities))

# Set edge weights based on Euclidean distance
for u, v in G.edges():
    G[u][v]['weight'] = distance(u, v)

# Algorithm BB to obtain a bottleneck-optimal biconnected subgraph
def algorithm_BB(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    H = nx.Graph()
    H.add_nodes_from(G.nodes())
    for u, v, data in edges_sorted:
        H.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(H):
            break
    return H

# Get the bottleneck-optimal biconnected subgraph
H = algorithm_BB(G)

# Finding a Hamiltonian cycle in the squared graph of the biconnected subgraph
H_squared = nx.power(H, 2)
tour = list(nx.approximation.traveling_salesman_problem(H_squared, cycle=True, weight='weight'))

# Calculate total cost and max distance of the tour
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))
max_distance = max(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))

# Correct tour to start and end at city 0 and reorder accordingly
start_index = tour.index(0)
reordered_tour = tour[start_index:] + tour[:start_index + 1]

# Final output
print("Tour:", reordered_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)