import math
import random
from itertools import permutations

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

# Groups of cities
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible combinations of visiting one city from each group
possible_combinations = [
    (g1, g2, g3)
    for g1 in groups[0]
    for g2 in groups[1]
    for g3 in groups[2]
]

# Initialize variables for minimum cost and the corresponding tour
min_cost = float('inf')
best_tour = None

# Evaluate each combination
for combination in possible_combinations:
    # Start and end at the depot (0)
    full_tour = [0] + list(combination) + [0]
    # Calculate the tour cost
    tour_cost = sum(distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour) - 1))
    
    # Update minimum cost and best tour if the current tour is better
    if tour_cost < min_cost:
        min_cost = tour_cost
        best_tour = full_tour

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))