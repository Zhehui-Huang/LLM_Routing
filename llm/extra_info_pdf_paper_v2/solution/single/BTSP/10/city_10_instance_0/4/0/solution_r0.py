import math
from scipy.spatial import distance_matrix
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Define the cities' coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create the distance matrix
n = len(cities)
dist_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i, j] = euclidean_distance(cities[i], cities[j])
        else:
            dist_matrix[i, j] = float('inf')

# Generating a minimum spanning tree
mst = minimum_spanning_tree(csr_matrix(dist_matrix))
tour = [0]  # Start at the depot city
remaining_cities = set(range(1, n))
current = 0

# Find a simple tour starting from the MST
while remaining_cities:
    # Find the closest city that is still remaining
    distances = {city: mst[current, city] if city in remaining_cities else float('inf') for city in range(n)}
    next_city = min(distances, key=distances.get)
    tour.append(next_city)
    remaining_cities.remove(next_city)
    current = next_city
tour.append(0)  # return to the depot

# Calculate the total travel cost and the maximum distance
total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)