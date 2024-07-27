import math
import numpy as np
from itertools import permutations


# Coordinates for the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate the Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Calculate the matrix of distances between all cities
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Generate all permutations of city visits (excluding the depot which is both start and end)
city_indices = list(range(1, n))  # Excludes depot city 0

min_max_distance = float('inf')
best_tour = None

# Check all possible permutations (brute force method)
for perm in permutations(city_indices):
    tour = [0] + list(perm) + [0]  # Create a tour that starts and ends at the depot
    max_dist_in_tour = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    if max_dist_in_tour < min_max_distance:
        min_max_distance = max_dist_in_tour
        best_tour = tour

# Calculate total distance of the best tour
total_cost = sum(distance_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")