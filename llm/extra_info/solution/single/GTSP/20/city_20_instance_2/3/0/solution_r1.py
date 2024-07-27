import itertools
import math

# Define city coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Define city groups
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Brute-force all combinations
all_combinations = itertools.product(*groups)
min_distance = float('inf')
best_tour = []

for combination in all_combinations:
    # Start from the depot, add one city from each group, return to the depot
    tour = [0] + list(combination) + [0]
    # Calculate the distance for this specific tour
    tour_distance = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    # Update the shortest tour found
    if tour_distance < min_distance:
        min_distance = tour_distance
        best_tour = tour

# Output the best tour and its total cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_distance, 2))