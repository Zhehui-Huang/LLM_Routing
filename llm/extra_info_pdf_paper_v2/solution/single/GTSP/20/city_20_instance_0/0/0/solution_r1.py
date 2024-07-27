import itertools
import math

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Groups of cities (except for the depot city 0)
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Compute Euclidean distances between all pairs of cities
def calculate_distance(city_a, city_b):
    xa, ya = cities[city_a]
    xb, yb = cities[city_b]
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

# Precompute distance matrix
n_cities = len(cities)
distance_matrix = [[calculate_distance(i, j) for j in range(n_cities)] for i in range(n_cities)]

# Calculate total travel distance for a given tour
def tour_distance(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Brute-force all combinations of city selections from each group
min_distance = float('inf')
best_tour = None

for combination in itertools.product(*groups):
    full_tour = [0] + list(combination) + [0]
    current_distance = tour_distance(full_tour)
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = full_tour

# Output results
print("Tour:", best_tour)
print("Total travel cost:", min_distance)