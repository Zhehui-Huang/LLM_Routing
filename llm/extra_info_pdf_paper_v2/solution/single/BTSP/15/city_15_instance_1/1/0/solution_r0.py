import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order
from collections import deque

# Cities' coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
    (83, 96), (60, 50), (98, 1)
]

# Number of cities
n = len(coordinates)

# Distance matrix
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = euclidean(coordinates[i], coordinates[j])

# Calculate MST
mst_matrix = minimum_spanning_tree(distance_matrix).toarray()
mst_matrix += mst_matrix.T  # Make symmetric to ease later processing

# Helper function to find a tour from the MST using pre-order traversal
def find_mst_tour(mst, start):
    visited = np.zeros(n, dtype=bool)
    tour = []

    def dfs(node):
        visited[node] = True
        tour.append(node)
        for neighbor in range(n):
            if mst[node, neighbor] > 0 and not visited[neighbor]:
                dfs(neighbor)
        tour.append(start)

    dfs(start)
    return tour[:-1]  # correcting for an extra return to start

# Derive the tour
tour = find_mst_tour(mst_matrix, 0)

# Calculate total travel cost and maximum distance between consecutive cities in the tour
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    d = euclidean(coordinates[tour[i-1]], coordinates[tour[i]])
    total_cost += d
    if d > max_distance:
        max_distance = d

# Since the tour returns to the start point
final_leg_distance = euclidean(coordinates[tour[-1]], coordinates[tour[0]])
total_cost += final_leg_distance
if final_leg_distance > max_distance:
    max_distance = final_leg_distance

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)