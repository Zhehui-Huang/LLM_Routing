import math
import networkx as nx

# Define the cities coordinates
cities = [
    (16, 90),  # City 0 (depot)
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Construct the graph G(V, E)
G = nx.Graph()
num_cities = len(cities)
for i in range(num_cities):
    for j in range(i+1, num_cities):
        G.add_edge(i, j, weight=distance(cities[i], cities[j]))

# Create a biconnected subgraph with minimized maximum edge weight (Algorithm BB)
edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
G_bb = nx.Graph()
G_bb.add_nodes_from(G.nodes())
for u, v, d in edges_sorted:
    G_bb.add_edge(u, v, weight=d['weight'])
    if nx.is_biconnected(G_bb):
        break

# Create a square graph of the biconnected subgraph
G_bb_square = nx.Graph()
for node in G_bb.nodes():
    neighbors = list(G_bb.neighbors(node))
    G_bb_square.add_node(node)
    for i in range(len(neighbors)):
        for j in range(i + 1, len(neighbors)):
            G_bb_square.add_edge(neighbors[i], neighbors[j], weight=distance(cities[neighbors[i]], cities[neighbors[j]]))

# Find Hamiltonian path in the squared graph G_bb_square
# Using TSP approximation since we need minimum tour length
tsp_path = nx.approximation.traveling_salesman_problem(G_bb_square, cycle=True)

# Collect tour data
tour = [0] + tsp_path + [0]
tour_cost = sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
max_distance = max(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Print the results
print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")