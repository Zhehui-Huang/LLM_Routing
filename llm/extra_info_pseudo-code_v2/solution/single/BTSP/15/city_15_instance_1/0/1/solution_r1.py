import math
import networkx as nx

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1),
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Build the graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            dist = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)

# Sort edges by weight
edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
subgraph = nx.Graph()
subgraph.add_nodes_from(G.nodes())

# Construct a biconnected subgraph based on the sorted edges
for edge in edges_sorted:
    subgraph.add_edge(edge[0], edge[1])
    if nx.biconnected.is_biconnected(subgraph):
        break

# Try to find the optimal tour
tour = list(nx.algorithms.approximation.traveling_salesman_problem(subgraph, cycle=True, weight='weight'))

# Calculate the total travel cost and max distance
total_cost = 0
max_distance = 0

for i in range(len(tour) - 1):
    dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    total_cost += dist
    max_distance = max(max_distance, dist)

# Closing the tour and ensuring it ends at the depot city
tour.append(tour[0])  # Complete the cycle to return to the depot city
closing_dist = euclidean_distance(cities[tour[-2]], cities[tour[-1]])
total_cost += closing﷯_dist
max_distance = max(max_distance, closing_dist)

# Results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_tfxtance:.2f}")