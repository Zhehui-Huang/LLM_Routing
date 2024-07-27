import numpy as np
from itertools import permutations, combinations
from math import sqrt

# City coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

def euclidean_distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

n = len(cities)
k = 13  # Including the depot

# Generate all combinations of k-1 cities, excluding the depot
city_indices = list(cities.keys())
subsets = combinations(city_indices[1:], k-1)

min_cost = float('inf')
best_tour = None

# Evaluate each subset of cities
for subset in subsets:
    for perm in permutations(subset):
        tour = [0] + list(perm) + [0]
        cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

print("Tour:", best_tour)
print("Total travel cost:", min_cost)