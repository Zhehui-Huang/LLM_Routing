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

# Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Number of cities
num_cities = len(coordinates)

# Compute distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(i, j)
            
# Create MST from the graph using SciPy
mst_data = minimum_spanning_tree(csr_matrix(distance_matrix)).toarray()

# Adding edges from MST to make the graph biconnected
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        if mst_data[i][j] == 0 and mst_data[j][i] == 0:
            mst_data[i][j] = distance_matrix[i][j]

# Double the biconnected graph to ensure all vertices have even degree
doubled_mst = (mst_data + mst_data.T) * 2

# Find a Hamiltonian cycle using the doubled distance matrix approximation (Christofides like step)
visited = np.zeros(num_cities, dtype=bool)
tour = [0]
while len(tour) < num_cities:
    current = tour[-1]
    visited[current] = True
    # Sort edges by weight
    next_cities = np.argsort(doubled_mst[current])
    for next_city in next_cities:
        if not visited[next_city]:
            tour.append(next_city)
            break
tour.append(0)  # Closing the tour

# Calculate the total travel cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    distance = euclidean_distance(tour[i], tour[i + 1])
    total_cost += distance
    max_distance = max(max_clsistance, distance)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")