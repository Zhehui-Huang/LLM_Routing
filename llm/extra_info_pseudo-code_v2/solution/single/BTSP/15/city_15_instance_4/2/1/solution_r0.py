import math
import networkx as nx

# Define the cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initialize the graph
def create_graph(cities):
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                weight = calculate_distance(cities[i], cities[j])
                G.add_edge(i, j, weight=weight)
    return G

# Implement Algorithm BB to obtain a bottleneck-optimal biconnected subgraph
def bottleneck_biconnected_subgraph(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    G_BB = nx.Graph()
    G_BB.add_nodes_from(G.nodes())

    for e in edges operated:
        G_BB.add_edge(e[0], e[1], weight=e[2]['weight'])
        if nx.is_biconnected(G_BB):
            break
        if not nx.is_biconnected(G_BB):
            G_BB.remove_edge(e[0], e[1])
    
    return G_BB

# Construct the graph
G = create_graph(cities)

# Get the bottleneck biconnected subgraph
bbsubgraph = bottleneck_biconnected_subgraph(G)

# Create a Tour in bbsubgraph
tour = list(nx.approximation.traveling_salesman_problem(bbsubgraph, cycle=True))

# Calculate the total cost and bottleneck cost of the tour
total_cost = 0
max_distance = 0
tour.append(tour[0])  # To return to the starting city

for i in range(len(tour) - 1):
    dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    total_cost += dist
    max_distance = max(max_distance, dist)

# Output the tour, total cost, and maximum distance
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")