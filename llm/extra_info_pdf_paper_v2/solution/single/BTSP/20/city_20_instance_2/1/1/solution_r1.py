import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# City coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate Euclidean distance
def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix creation
num_cities = len(coordinates)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i][j] = euclidean_dist(coordinates[i], coordinates[j])

# MST solution based on the distance matrix
mst = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()
tour = []
visited = [False] * num_cities

# Helper function to perform DFS and extract a tour from MST
def extract_tour(curr_node):
    visited[curr_node] = True
    tour.append(curr_node)
    for neighbor in range(num_cities):
        if mst[curr_node][neighbor] > 0 and not visited[neighbor]:
            extract_tour(neighbor)

# Starting DFS from the depot (node 0)
extract_tour(0)

# Adding depot city to the end to complete the cycle
tour.append(0)

# Calculate tour cost and maximum edge distance
total_cost = 0
max_edge_dist = 0
for i in range(len(tour)-1):
    dist = euclidean_dist(coordinates[tour[i]], coordinates[tour[i+1]])
    total_cost += dist
    if dist > max_edge_dist:
        max_edge_dist = dist

# Outputs
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_edge_dist)