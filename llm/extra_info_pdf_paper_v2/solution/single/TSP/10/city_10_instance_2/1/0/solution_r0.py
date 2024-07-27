import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculates the Euclidean distance between two cities
def distance(a, b):
    return euclidean(cities[a], cities[b])

# Number of cities
num_cities = len(cities)

# Distances between each pair of cities
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i, j] = distance(i, j)

# Generate all permutations of the cities except the depot (city 0)
city_indices = list(range(1, num_cities))  # cities except the depot
perms = permutations(city_indices)

# Evaluating all permutations to find the minimum distance tour
min_distance = float('inf')
best_tour = None

for perm in perms:
    # Start at the depot (0), go through the permutation of cities, and back to the depot (0)
    tour = [0] + list(perm) + [0]
    # Calculate the total travel cost of this tour
    tour_distance = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    # If this tour has a shorter total travel cost, update the best found
    if tour_distance < min_distance:
        min_distance = tour_distance
        best_tour = tour

# Result output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance}")