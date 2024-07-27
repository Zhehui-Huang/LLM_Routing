import math
from itertools import permutations

# City coordinates
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Number of cities
n = len(coordinates)

# Compute the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Precompute distances between all city pairs
dist_matrix = [[distance(i, j) for j in range(n)] for i in range(n)]

# Create a naive BTSP tour by considering each permutation (feasible only for small input sizes)
def find_btsp_tour():
    best_tour = None
    best_cost = float('inf')
    best_max_dist = float('inf')

    for perm in permutations(range(1, n)):
        current_tour = [0] + list(perm) + [0]
        # Calculate tour cost and max distance for the current tour
        max_dist = 0
        total_cost = 0
        for i in range(len(current_tour) - 1):
            d = dist_matrix[current_tour[i]][current_tour[i + 1]]
            total_cost += d
            max_dist = max(max_dist, d)

        # Update the best tour if current one is better
        if max_dist < best_max_dist:
            best_tour = current_tour
            best_cost = total_cost
            best_max_dist = max_dist

    return best_tour, best_cost, best_max_dist

# Find the BTSP tour
tour, total_cost, max_distance = find_btsvp_tour()

# Output the result
print('Tour:', tour)
print('Total travel cost:', total_cost)
print('Maximum distance between consecutive cities:', max_distance)