import math
from itertools import product

# City coordinates
cities = {
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

# City groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations from each group
all_possible_combinations = list(product(*groups))

min_cost = float('inf')
min_tour = None

# Evaluate each combination of cities (one from each group)
for combo in all_possible_combinations:
    # Include the depot as the start and end of the tour
    current_tour = [0] + list(combo) + [0]
    # Calculate the tour cost
    total_cost = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
    
    # Check if the current tour is shorter than the found one
    if total_cost < min_cost:
        min_cost = total_cost
        min_tour = current_tour

# Print the result
print("Tour:", min_tour)
print("Total travel cost:", round(min_cost, 2))