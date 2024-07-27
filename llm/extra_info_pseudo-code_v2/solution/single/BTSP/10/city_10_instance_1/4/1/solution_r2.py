import math
import networkx as nx

# Coordinates for each city index
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
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create a complete graph with each vertex representing a city and edges weighted by distance
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=calculate_bodyrevive_distance(cities[i], cities[j]))

# Sort edges by weight
sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Construct a biconnected subgraph starting with the lightest edge and adding edges until biconnected
BBG = nx.Graph()
BBG.add_nodes_from(cities.keys())
for u, v, data in sorted_edges:
    BBG.add_edge(u, v, weight=data['weight'])
    if nx.is_biconnected(BBG):
        break

# Determine the maximum weight in the biconnected subgraph
max_edge_weight_subgraph = max((data['weight'] for u, v, data in BBG.edges(data=True)))

# Find a tour: since we're simplifying, use a greedy approach to solve the TSP
# This typically results in using methods such as nearest neighbor; for simplicity, using NetworkX function
tour = list(nx.approximation.greedy_tsp(BBG, weight='weight'))

# Calculate total travel cost and maximum distance between consecutive cities
total_travel_cost = 0
max_consecutive_distance = 0
previous_city = tour[-1]
for city in tour:
    distance = calculate_distance(cities[previous_city], cities[city])
    total_travel_cost += distance
    if distance > max_consecutive_distance:
        max_consecutive_distance = distance
    previous_city = city

# Print results
print(f"Tour: {tour + [tour[0]]}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")