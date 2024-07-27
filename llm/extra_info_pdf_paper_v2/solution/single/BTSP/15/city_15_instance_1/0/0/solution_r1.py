import math
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np
from itertools import permutations

# City coordinates
coords = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate distance matrix
dist_matrix = distance_matrix(coords, coords)

# Use Minimum Spanning Tree (MST) to find an approximation
mst = minimum_spanning_tree(dist_matrix)

# Convert MST to a dense format for traversal
mst_dense = mst.toarray().astype(float)

# Double all edges in MST (convert to Eulerian graph)
doubled_edges = mst_dense + mst_dense.T

def dfs_cycle(graph, start):
    """ Helper function to perform DFS and find a cycle """
    n = len(graph)
    visited = [False] * n
    tour = []
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            tour.append(node)
            for neighbor in reversed(range(n)):
                if graph[node][neighbor] > 0 and not visited[neighbor]:
                    stack.append(neighbor)
    return tour

# Find a cycle using DFS on the MST
tour = dfs_cycle(doubled_edges, 0)
# Append the start city to complete the cycle
tour.append(0)

# Calculate the cost of the tour
total_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Calculate the maximum distance between consecutive cities in the tour
max_distance = max(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Display results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)