import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np

# Coordinate data for cities including the depot city
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
    (60, 63), (93, 15)
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Number of cities including the depot
num_cities = len(coordinates)

# Creating a distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Using SciPy to find the Minimal Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(csr_matrix(distance_matrix))

# Helper function to perform DFS traversal to order the nodes (Preorder DFS)
def dfs_order(graph, start, visited=None, order=None):
    if visited is None:
        visited = [False] * num_cities
    if order is None:
        order = []

    visited[start] = True
    order.append(start)
    for nbr in range(num_cities):
        if graph[start, nbr] != 0 and not visited[nbr]:
            dfs_order(graph, nbr, visited, order)
    return order

# Getting an approximate TSP tour by performing a DFS on the MST
tour = dfs_order(mst_matrix, 0)

# Ensuring we return to the starting point (depot city)
tour.append(0)

# Computing the total travel distance of the tour
total_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)