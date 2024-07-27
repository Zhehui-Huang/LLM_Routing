import math
import numpy as np

# Coordinates of all cities including the depot
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Total number of cities
n = len(cities)

# Generate all possible tours starting and ending at the depot, visiting others exactly once
from itertools import permutations

min_max_dist = float('inf')
best_tour = None

for perm in permutations(range(1, n)):  # Generate permutations of cities 1 through 14
    tour = [0] + list(perm) + [0]
    max_dist = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if max_dist < min_max_dist:
        min_max_dist = max_dist
        best_tour = tour

# Calculate total travel cost for the best tour found
total_cost = sum(euclidean_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_dist:.2f}")