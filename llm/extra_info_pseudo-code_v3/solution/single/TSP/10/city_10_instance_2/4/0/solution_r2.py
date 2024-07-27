import numpy as np
from scipy.spatial.distance import euclidean
import networkx as nx
from networkx.algorithms.approximation.traveling_salesman import christofides

# Coordinates of the cities
city_coords = np.array([
    [90, 3],   # Depot city 0
    [11, 17], 
    [7, 27], 
    [95, 81], 
    [41, 54], 
    [31, 35], 
    [23, 95], 
    [20, 56], 
    [49, 29], 
    [13, 17]
])

# Generate a complete graph from these cities
G = nx.complete_graph(len(city_coords))

# Set the weights (distances) on the graph edges
for i in range(len(city_coords)):
    for j in range(i + 1, len(city_coords)):
        G[i][j]['weight'] = euclidean(city_coords[i], city_coords[j])

# Use the Christofides algorithm to find a tour
tour = christofides(G, weight='weight')

# Include the tour returning to the depot:
if tour[-1] != 0:
    tour.append(0)

# Calculate the total cost of the tour
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

# Display the results
print("Tour:", tour)
print("Total travel cost:", total_cost)