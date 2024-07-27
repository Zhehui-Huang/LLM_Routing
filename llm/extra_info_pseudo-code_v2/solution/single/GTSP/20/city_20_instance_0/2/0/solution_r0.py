import numpy as np

# City coordinates with index as city number
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

# City groups
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def calculate_total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Brute force approach to find the shortest possible tour visiting one city from each group
best_tour = None
min_cost = float('inf')

import itertools

for comb in itertools.product(*groups):
    full_tour = [0] + list(comb) + [0]
    cost = calculate_total_distance(full_tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = full_tour

print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))