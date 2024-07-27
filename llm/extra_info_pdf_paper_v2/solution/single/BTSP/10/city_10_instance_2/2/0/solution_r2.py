import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order
from scipy.sparse import csr_matrix

# Coordinates of the cities
coordinates = [
    (90, 3),  # Depot
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 44),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29), 
    (13, 17)
]

# Function to calculate the Euclidean distance
def euclidean_distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# Number of cities
n = len(coordinates)

# Create a distance matrix
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            distance_matrix[i][j] = float('inf')

# Convert the distance matrix to a CSR matrix and find the minimum spanning tree
mst = minimum_spanning_tree(csr_matrix(distance_matrix))

# Order cities with a DFS, starting from city 0, ensuring the tour starts and ends at the city 0
visited = np.zeros(n, dtype=bool)
stack = [0]
tour = []

while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        tour.append(node)
        # Push adjacent nodes in the MST to the stack
        connections = mst[node].nonzero()[1]
        for connected_node in connections:
            if not visited[connected_node]:
                stack.append(connected_node)
tour.append(0)  # Return to the depot

# Calculate total and maximum travel distances
total_distance = 0
max_distance = 0
for i in range(1, len(tour)):
    dist = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    total_distance += dist
    if dist > max_distance:
        max_distance = dist

# Formatting the output for clarity
output_tour = f"Tour: {tour}"
output_total_distance = f"Total travel cost: {total_distance:.2f}"
output_max_distance = f"Maximum distance between consecutive cities: {max_duration:.2f}"

print(output_tour)
print(output_total_distance)
print(output_max_distance)