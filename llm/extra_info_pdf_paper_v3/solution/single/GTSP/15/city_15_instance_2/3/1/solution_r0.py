import math
from itertools import product

# Cities with coordinates
coordinates = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Groups of city indices
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Compute the possible tours and pick the shortest one
def find_optimal_tour():
    all_combinations = list(product(*groups))
    min_distance = float('inf')
    optimal_tour = None

    # Evaluate all combinations of cities taking one from each group
    for combination in all_combinations:
        current_tour = [0] + list(combination) + [0]
        total_dist = sum(distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
        
        if total_dist < min_distance:
            min_distance = total_dist
            optimal_tour = current_tour

    return optimal_tour, min_distance

# Finding the optimal tour
tour, total_cost = find_optimal_tour()

# Output the results as specified
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")