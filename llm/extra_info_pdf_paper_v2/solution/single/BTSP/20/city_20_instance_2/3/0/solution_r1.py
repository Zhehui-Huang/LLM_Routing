import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np

# Coordinates of the cities (including the depot)
coordinates = [
    (3, 26),  # Depot city
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

# Helper function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Number of cities, including the depot
n_cities = len(coordinates)

# Create a distance matrix
distance_matrix = [[euclidean_distance(i, j) for j in range(n_cities)] for i in range(n_cities)]

# Create a minimum spanning tree (MST) from the distance matrix
mst = minimum_spanning_tree(csr_matrix(distance_matrix)).toarray()

# Depth-First Search to get the tour from MST
def dfs_tour_from_mst(start_node, mst, visited):
    stack = [start_node]
    tour = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            tour.append(node)
            # Add nodes in reverse order to visit the smallest index last
            for neighbor, has_edge in enumerate(reversed(mst[node])):
                if has_edge and not visited[len(mst) - 1 - neighbor]:
                    stack.append(len(mst) - 1 - neighbor)
    return tour

# Initial call to the DFS function
visited = [False] * n_cities
tour = dfs_tour_from_mst(0, mst, visited)
tour.append(0)  # To return to the start (depot)

# Calculate total cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    dist = euclidean_distance(tour[i], tour[i + 1])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)