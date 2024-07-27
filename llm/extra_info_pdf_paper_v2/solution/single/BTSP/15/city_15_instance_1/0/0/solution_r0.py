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

# Create a tour from MST using a simple traversal (DFS)
def create_tour(matrix, start=0):
    n = len(matrix)
    visited = [False] * n
    tour = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            tour.append(node)
            # Add all connected non-visited nodes to the stack
            for neighbor in range(n-1, -1, -1):  # reverse order to keep correct path
                if matrix[node][neighbor] != 0 and not visited[neighbor]:
                    stack.append(neighbor)
    
    tour.append(start)  # return to the start
    return tour

tour = create_tour(doubled_edges)

# Calculate the cost of the tour
total_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Calculate the maximum distance
max_distance = max(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

result = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

result