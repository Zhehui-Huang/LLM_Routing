import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# City coordinates
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Euclidean distance function
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Construct distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(i, j)
        else:
            distance_matrix[i][j] = float('inf')

# Minimum spanning tree
mst_matrix = minimum_spanning_tree(csr_matrix(distance_matrix)).toarray()

# Create a double tree to ensure all vertices connecting doubly
mst_double = mst_matrix + mst_matrix.T

# Creating tour from double tree by Preorder DFS starting from the depot
def dfs_preorder(start, graph, visited):
    visited[start] = True
    path = [start]
    for i in range(len(graph)):
        if graph[start][i] != 0 and not visited[i]:
            path.extend(dfs_preorder(i, graph, visited))
    return path

visited = np.zeros(num_cities, dtype=bool)
tour = dfs_preorder(0, mst_double, visited)

# Ensure the tour completes (return to start if not present)
if tour[0] != tour[-1]:
    tour.append(tour[0])

# Calculate costs along the tour
total_cost = 0
max_edge_cost = 0

for i in range(1, len(tour)):
    dist = euclidean_distance(tour[i - 1], tour[i])
    total_cost += dist
    if dist > max_edge_cost:
        max_edge_cost = dist

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_edge_cost:.2f}")