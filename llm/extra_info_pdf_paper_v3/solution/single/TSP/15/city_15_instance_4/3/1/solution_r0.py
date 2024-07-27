import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.spatial.distance import pdist, squareform
import numpy as np

# Coordinates of the cities
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate all pairwise Euclidean distances
coords_matrix = np.array(coordinates)
distance_matrix = squareform(pdist(coords_matrix, metric='euclidean'))

# Create a symmetric matrix because our graph is undirected
distance_matrix = (distance_matrix + distance_matrix.T) / 2

# Compute the minimum spanning tree
mst_matrix = minimum_spanning_tree(distance_matrix).toarray()
# Because the MST will have one entry per edge, we make it symmetric
mst_matrix += mst_matrix.T

def dfs(mst_matrix, start):
    """ Depth-first search to walk through the MST and construct a tour """
    n = len(mst_matrix)
    visited = [False] * n
    tour = []

    def recurse(vertex):
        visited[vertex] = True
        tour.append(vertex)
        for neighbor in range(n):
            if mst_matrix[vertex, neighbor] != 0 and not visited[neighbor]:
                recurse(neighbor)
                tour.append(vertex)  # return to current vertex
    
    recurse(start)
    return tour

# Get a double-cover of the MST using DFS, then make it a simple tour
tour_mst = dfs(mst_matrix, 0)
tour = []
visited = [False] * len(coordinates)

for city in tour_mst:
    if not visited[city]:
        tour.append(city)
        visited[city] = True
tour.append(tour[0])  # Returning to the depot city

# Calculate the total cost of the tour
total_cost = sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")