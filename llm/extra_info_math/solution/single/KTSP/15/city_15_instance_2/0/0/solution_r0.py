import math
import itertools
import numpy as np

# City coordinates, indexed from 0 to 14
cities_coordinates = [
    (54, 87), # Depot city 0
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# Number of cities to visit including the depot
k = 8

# Calculate Euclidean distance between two cities
def euc_dist(i, j):
    (x1, y1) = cities_coordinates[i]
    (x2, y2) = cities_coordinates[j]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate matrix with distances between all pairs of cities
n = len(cities_coordinates)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i][j] = euc_dist(i, j)

# Function to calculate total distance of a tour
def total_distance(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += dist_matrix[tour[i]][tour[i+1]]
    return total_dist

# Find the shortest tour using a brute force approach over combinations
min_tour = None
min_tour_length = float('inf')

for cities in itertools.combinations(range(1, n), k-1):  # choose k-1 cities because depot is fixed
    current_tour = [0] + list(cities) + [0]
    for permutation in itertools.permutations(current_tour[1:-1]):
        perm_tour = [0] + list(permutation) + [0]
        tour_length = total_distance(perm_tour)
        if tour_length < min_tour_length:
            min_tour_length = tour_length
            min_tour = perm_tour

# Output the result
print("Tour:", min_tour)
print("Total travel cost:", min_tour_length)