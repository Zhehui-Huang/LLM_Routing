import math
import networkx as nx

# Coordinates for each city
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
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Constructing the full graph with computed distances
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=calculate_distance(cities[i], cities[j]))

# Sorting edges by weight for use in bottleneck biconnected subgraph approach
edges_sorted_by_weight = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Subgraph for biconnectivity analysis
E_BB = nx.Graph()
E_BB.add_nodes_from(G.nodes)

# Include edges until the subgraph is biconnected
for u, v, d in edges_sorted_by_weight:
    E_BB.add_edge(u, v, weight=d['weight'])
    if nx.is_biconnected(E_BB):
        break

# Determining the tour using a simple greedy TSP approach in the biconnected subgraph
tour = list(nx.approximation.traveling_salesman_problem(E_BB, cycle=True, method='greedy'))

# Calculate the total travel cost and the max distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(len(tour)):
    next_city = tour[(i+1) % len(tour)]  # wrap around to start for the last element
    dist = calculate_distance(cities[tour[i]], cities[next_city])
    total_cost += dist
    max_distance = max(max_distance, dist)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")