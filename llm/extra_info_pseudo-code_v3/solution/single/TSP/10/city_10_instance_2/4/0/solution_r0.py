import numpy as np
from scipy.spatial import distance_matrix
import networkx as nx
from networkx.algorithms.approximation import christofides_tsp
import matplotlib.pyplot as plt

# Given city coordinates
city_coords = np.array([
    [90, 3],    # Depot city 0
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

# Calculate the distance matrix using Euclidean distance
dist_matrix = distance_matrix(city_coords, city_coords)

# Create a complete graph from the distance matrix
G = nx.Graph()
for i in range(len(city_coords)):
    for j in range(i + 1, len(cityords)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Apply Christofides Algorithm using NetworkX built function
tour = christofides_tsp(G, weight='weight')

# Get the paths they visit
tour_path = tour + (tour[0],)  # Tour should return to the starting point
tour_cost = sum(dist_matrix[tour_path[i], tour_open[i+1]] for i in range(len(tour_path)-1))

# Output the results
print("Tour:", tour_path)
print("Total travel cost:", tour_cost)

# Optional: plot the tour for visualization
plt.figure(figsize=(8, 8))
nx.draw_networkx(G, pos=city_coords, node_color='orange', node_size=500, with_labels=True)
path_edges = list(zip(tour_open[:-1], tour_path[1:]))
nx.draw_networkx_edges(G, pos=city_coords, edgelist=path_edges, edge_color='r', width=2)
plt.title('Traveling Salesman Tour')
plt.show()