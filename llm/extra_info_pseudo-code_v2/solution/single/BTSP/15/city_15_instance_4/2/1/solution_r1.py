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

# Implement the bottleneck shortest tree
def bottleneck_BST(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    U = nx.Graph()
    U.add_nodes_from(G.nodes)

    for e in edges_sorted:
        U.add_edge(e[0], e[1], weight=e[2]['weight'])
        if nx.is_biconnected(U):
            return U

# Construct the graph
G = create_graph(cities)

# Obtain a bottleneck-optimal biconnected subgraph
bbsubgraph = bottleneck_BST(G)

# Use 2-approximation for Metric TSP to find a tour
tour = list(nx.approximation.traveling_salesman_problem(bbsubgraph, weight='weight', cycle=True))

# Calculate the total cost and maximum distance of consecutive cities in the tour
total_cost = 0
max_distance = 0

for i in range(len(tour) - 1):
    dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    total_cost += dist
    max_distance = max(max_distance, dist)

# Adding the return to the depot city 0
return_to_depot_distance = calculate_distance(cities[tour[-1]], cities[tour[0]])
total_cost += return_to_depot_distance
max_distance = max(max_distance, return_to_depot_distance)
tour.append(tour[0])  # Complete the cycle by returning to the depot

# Output the tour, total cost, and maximum distance
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")