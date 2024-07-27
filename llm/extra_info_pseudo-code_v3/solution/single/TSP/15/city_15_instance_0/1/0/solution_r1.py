import math
import networkx as nx
from networkx.algorithms.approximation import christofides

# Define city coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            dist = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)

# Apply Christofides' algorithm to find an approximate solution to the TSP
tour = christofides(G)

# Calculate the tour's total weight
total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
total_cost += euclidean_distance(cities[tour[-1]], cities[tour[0]])  # To add the cost of returning to the starting point

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)