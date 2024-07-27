import numpy as np
import networkx as nx

# Define the coordinates of the depot and cities
coordinates = [
    (16, 90),  # Depot City 0
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

# Compute Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a fully connected graph
G = nx.complete_graph(len(coordinates))

# Add edges between all nodes with weights as the Euclidean distances
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        distance = euclidean_distance(coordinates[i], coordinates[j])
        G.add_edge(i, j, weight=distance)
        G.add_edge(j, i, weight=distance)

# Use NetworkX to find an approximation to the TSP
path = nx.approximation.traveling_salesman_problem(G, cycle=True, weight='weight')

# Compute the total travel cost of the tour
total_cost = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))

# Output the result
print(f"Tour: {path}")
print(f"Total travel cost: {total_cost:.2f}")