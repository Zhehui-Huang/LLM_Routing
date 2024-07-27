import networkx as nx
import numpy as np
from scipy.spatial.distance import euclidean

# Coordinates of cities
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

# Function to compute Euclidean distance between two cities by ID
def compute_distance(city1_id, city2_id):
    return euclidean(cities[city1_id], cities[city2_id])

# Creating a complete weighted graph
G = nx.Graph()
for city1 in cities:
    for city2 in cities:
        if city1 != city2:
            dist = compute_distance(city1, city2)
            G.add_edge(city1, city2, weight=dist)

# Applying the Christofides algorithm to find an approximate solution
tour = nx.approximation.traveling_salesman.christofides(G, weight='weight')

# Calculate the total cost of the tour
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

# Ensure the tour starts and ends at the depot city 0
if tour[0] != 0:
    zero_index = tour.index(0)
    tour = tour[zero_index:] + tour[:zero_index]
if tour[-1] != 0:
    tour.append(0)

# Output the tour and total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)