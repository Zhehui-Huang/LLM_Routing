import networkx as nx
import numpy as np
from scipy.spatial.distance import euclidean
from networkx.algorithms.approximation import christofides_tsp

# Define the coordinates of the cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Create a function to compute the Euclidean distance between two cities
def compute_distance(city1_id, city2_id):
    city1 = cities[city1_id]
    city2 = cities[city2_id]
    return euclidean(city1, city2)

# Create a complete graph G for the 10 cities
G = nx.complete_graph(len(cities))

# Add weights (Euclidean distances) to the edges of the graph
for u, v in G.edges():
    G[u][v]['weight'] = compute_distance(u, v)

# Apply the Christofides algorithm to find a solution
tour = christofides_tsp(G, weight='weight')

# Calculate the total cost of the found tour
total_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Since the Christofides algorithm does not always start from the required city 0,
# Ensure the tour starts and ends at city 0
start_index = tour.index(0)
shifted_tour = tour[start_index:] + tour[:start_index] + [0]

# Print the output as per the format requirements
print("Tour:", shifted_tour)
print("Total travel cost:", total_cost)