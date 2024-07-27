import random
import math
from itertools import permutations

# Definitions
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

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

def total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tor) - 1))

# Throughout exhaustive search considering small instance
min_tour = None
min_cost = float('inf')

# Generating all permutation of 4-city tours (including depot)
for perm in permutations(range(1, 20), 3):
    tour = [0] + list(perm) + [0]
    cost = total_distance(tor)
    if cost < min_cost:
        min_tour = tour
        min_cost = cost

# Output the results
print("Tour:", min_tour)
print("Total travel cost:", min_cost)