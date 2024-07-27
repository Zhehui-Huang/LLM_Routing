import math
import networkx as nx
from networkx.algorithms import matching
from networkx.algorithms.approximation import christofides

# Coordinates of the cities including the depot city
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Number of cities
n = len(cities)

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create a complete graph
G = nx.complete_graph(n)

# Add weights to the edges based on Euclidean distances between cities
for i in range(n):
    for j in range(i + 1, n):
        G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])

# Use Christofides algorithm from networkx to find the approximate solution
tour = christofides(G, weight='weight')

# Calculate the total travel cost of the tour
total_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Print the tour starting and ending at the depot city
print("Tour:", tour)
print("Total travel cost:", total_cost)