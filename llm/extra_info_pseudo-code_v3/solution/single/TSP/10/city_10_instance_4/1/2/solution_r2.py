import math
import networkx as nx
from networkx.algorithms.approximation import christofides

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# City coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62),
]

# Step 1: Construct complete graph G with Euclidean distances
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(len(cities)):
        if i != j:
            G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])

# Using the Christofides algorithm to find an approximate solution
tour = christofides(G, weight='weight')

# Calculate total travel cost
total_cost = 0
for i in range(1, len(tour)):
    total_cost += G[tour[i-1]][tour[i]]['weight']
# Add the return to the starting city (depot)
total_cost += G[tour[-1]][tour[0]]['weight']

# Include the return to starting city in the tour
tour.append(tour[0])

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)