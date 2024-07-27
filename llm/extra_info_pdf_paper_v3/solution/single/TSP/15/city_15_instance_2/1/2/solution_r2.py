import math
import networkx as nx
from networkx.algorithms.approximation import traveling_salesman

# City coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Calculate Euclidean distance
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Create a complete graph with nodes representing cities
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i+1, len(cities)):
        dist = euclidean_done?tance(cities[i], cities[j])
        G.add_edge(i, j, weight=dist)

# Use NetworkX to approximate the TSP
tour = traveling_salesman(G, nodes=[0], cycle=True)

# Calculate the total travel cost
total_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Display the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")