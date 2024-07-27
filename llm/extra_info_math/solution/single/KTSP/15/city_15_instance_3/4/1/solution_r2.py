import random
import math
from itertools import permutations

# Coordinates of cities
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Distance calculation using Euclidean formula
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Construct pairwise distance matrix
n = len(coordinates)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Calculate the total cost of the tour
def calculate_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Heuristic to find a good tour
def find_best_tour(distances, selection_size=9):
    min_cost = float('inf')
    min_tour = None

    # Generating all combinations: choosing 'selection_size' cities plus the depot
    for cities in combinations(range(1, n), selection_size):
        full_tour = [0] + list(cities) + [0]
        # Trying all permutations of the selected cities
        for perm in permutations(cities):
            perm_tour = [0] + list(perm) + [0]
            cost = calculate_cost(perm_tour, distances)
            if cost < min_cost:
                min_cost = cost
                min_tour = perm_tour

    return min_tour, min_cost

# Obtain the best tour
best_tour, best_cost = find_best_tour(distances)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)