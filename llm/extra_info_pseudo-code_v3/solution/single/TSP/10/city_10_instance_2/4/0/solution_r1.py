import numpy as np
from scipy.spatial.distance import euclidean
import networkx as nx
from networkx.algorithms.approximation.traveling_salesman import christofides

# Coordinates of the cities
city_coords = np.array([
    [90, 3],  # Depot city 0
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

# Construct a complete graph with each city as a node
G = nx.complete_graph(len(city_coords))
for i in range(len(city_coords)):
    for j in range(i + 1, len(city_coords)):
        # Add the Euclidean distance as the edge weight between every pair of cities
        G.edges[i, j]['weight'] = euclidean(city_coords[i], city_coords[j])

# Use Christofides algorithm for an approximate solution
tour = christofides(G, weight='weight')

# Ensure the tour starts and ends at the depot city 0
# As christofides algorithm might not start with the depot city
if tour[0] != 0:
    # Rotate the list so that it starts with the depot city 0
    zero_index = tour.index(0)
    tour = tour[zero_index:] + tour[:zero_index]
tour.append(0)  # Return to the depot

# Calculating the total cost of the tour
total_cost = sum(G[tour[i]][tour[i + 1]]['Cristofides algorithm for an approximate imple'] for i in range(len(tour) - 1))

# Output the tour and the total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)