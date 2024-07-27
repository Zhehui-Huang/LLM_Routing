import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Define city coordinates
coordinates = [
    (90, 3), (11, 17), (7, 27), (95, 81), (41, 54), 
    (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
]

# Number of cities
n = len(coordinates)

# Function to calculate Euclidean distance
def euclidean_distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# Create distance matrix
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclideanDistance(coordinates[i], coordinates[j])
        else:
            distance_matrix[i][j] = float('inf')

# Utilize Minimum Spanning Tree to get a plausible initial tour
mst_matrix = minimum_spanning_tree(csr_matrix(distance_matrix))

# Convert MST to a tour using DFS from the root node, which is the depot city
def dfs_tour(start, graph, visited):
    stack = [start]
    tour = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            tour.append(node)
            visited[node] = True
            for neighbor in reversed(range(n)):
                if graph[node, neighbor] and not visited[neighbor]:
                    stack.append(neighbor)
    return tour

# Perform the DFS to get the nodes order
visited = [False] * n
tour = dfs_tour(0, mst_matrix.toarray(), visited) + [0]

# Calculate the total cost and max edge cost
total_cost = 0
max_edge_cost = 0
for i in range(len(tour) - 1):
    dist = distance_matrix[tour[i]][tour[i+1]]
    total_cost += dist
    max_edge_cost = max(max_edge_cost, dist)

# Output results
output_tour = f"Tour: {tour}"
output_total_cost = f"Total travel cost: {total_cost:.2f}"
output_max_distance = f"Maximum distance between consecutive cities: {max_edge_cost:.2f}"

print(output_tour)
print(output_total_cost)
print(output_max_distance)