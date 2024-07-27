import math
from itertools import product

# City coordinates, including the depot
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
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def evaluate_tour(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Generate all combinations of selecting one city from each group
all_combinations = list(product(*groups))

# Variable to store the minimum cost and corresponding tour
min_cost = float('inf')
best_tour = None

# Explore each combination
for combo in all_combinations:
    current_tour = [0] + list(combo) + [0]  # A tour that starts and ends at the depot
    cost = evaluate_tour(current_tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = current_tour

# Output the tour and the total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")