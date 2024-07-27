import math
import itertools
import random

# Distance function
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Cities coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Groups of cities
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Helper function to calculate total distance of the tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        total_distance += euclidean_distance(*cities[city_a], *cities[city_b])
    return total_distance

# Brute force attempt to find the optimal solution
best_tour = None
best_distance = float('inf')

# Generate all possible combinations, one from each group
for combination in itertools.product(*groups):
    current_tour = [0] + list(combination) + [0]
    current_distance = calculate_total_distance(current_tour)
    if current_distance < best_distance:
        best_tour = current_tour
        best_distance = current_distance

print("Tour:", best_tour)
print("Total travel cost:", best_distance)