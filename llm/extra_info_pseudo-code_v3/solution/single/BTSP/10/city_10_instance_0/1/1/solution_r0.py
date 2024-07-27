import itertools
from math import sqrt

# Coordinates of cities
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

# Calculating Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all permutations of city indices (excluding depot)
city_indices = list(cities.keys())[1:]

# Find the optimal tour that minimizes the maximum distance between consecutive cities
min_max_distance = float('inf')
optimal_tour = None

for perm in itertools.permutations(city_indices):
    tour = [0] + list(perm) + [0]
    max_distance = max(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        optimal_tour = tour

# Compute the total travel cost of the tour
total_cost = sum(calc_dist for i, calc_dist in enumerate(optimal_tour[:-1], 1))

# Provide the results
print(f'Tour: {optimal_tour}')
print(f'Total travel cost: {total_cost:.2f}')
print(f'Maximum distance between consecutive cities: {min_max_distance:.2f}')