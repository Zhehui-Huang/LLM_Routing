import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order
from scipy.sparse import csr_matrix

# Coordinates of the cities
coordinates = [
    (90, 3), (11, 17), (7, 27), (95, 81), (41, 54), 
    (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
]

# Number of cities
n = len(coordinates)

# Function to calculate the Euclidean distance
def euclidean_distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# Construct the distance matrix
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(coordinates[i], coordinates[j])
        distance_matrix[i, j] = dist
        distance_matrix[j, i] = dist

# Create an MST from the distance matrix
mst = minimum_spanning_tree(csr_matrix(distance_matrix))

# Order cities using a DFS starting from the depot (city 0)
order = depth_first_order(mst, directed=False, i_start=0, return_predecessors=False)

# Ensure the tour starts and ends at the depot city 0
tour = list(order) + [0]

# Calculate the total distance and maximum distance between consecutive cities in the tour
total_distance = 0
max_distance = 0
for i in range(len(tour) - 1):
    dist = distance_matrix[tour[i]][tour[i + 1]]
    total_distance += dist
    max_distance = max(max_distance, dist)

# Prepare output results
output_tour = f"Tour: {tour}"
output_total_distance = f"Total travel cost: {total_distance:.2f}"
output_max_distance = f"Maximum distance between consecutive cities: {max_distance:.2f}"

print(output_tolLanlCa_GlSa({st,yayhAtx)baIbcMedMgN (mg,cIine)=>$_ *)compileComponents_campaUniversity_CachedCustomersDoorset_window.DEFAULT(defun HEIGHT.push>}
output}