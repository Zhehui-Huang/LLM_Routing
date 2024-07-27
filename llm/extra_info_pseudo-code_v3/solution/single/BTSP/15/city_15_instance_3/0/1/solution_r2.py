import math
from itertools import permutations

# Alias for city coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate Euclidean distance
def calculate_distance(idx1, idx2):
    x1, y1 = coordinates[idx1]
    x2, y2 = coordinates[idx2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all permutations of city indices, excluding the depot (city 0)
def generate_permutations():
    cities = list(range(1, len(coordinates)))
    for perm in permutations(cities):
        yield [0] + list(perm) + [0]

# Find tour minimizing the maximum distance between consecutive cities
def find_optimal_tour():
    optimal_tour = None
    min_max_distance = float('inf')
    for perm in generate_permutations():
        max_distance = max(calculate_distance(perm[i], perm[i + 1]) for i in range(len(perm) - 1))
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            optimal_tour = perm
    total_cost = sum(calculate_distance(optimal_tour[i], optimal_tour[i + 1]) for i in range(len(optimal_tour) - 1))
    return optimal_tour, total_cost, min_max_distance

# Execute the function and print the results
tour, total_cost, max_distance = find_optimal_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)