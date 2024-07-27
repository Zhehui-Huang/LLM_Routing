import itertools
import math

# Given coordinates of the cities
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

# Groups of cities
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 15, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Find all combinations of one city per group
all_combinations = itertools.product(*groups)

min_cost = float('inf')
optimal_tour = None

# Iterate through each combination and find the optimal tour
for combination in all_combinations:
    # Creating a tour starting and ending at the depot
    tour = [0] + list(combination) + [0]
    cost = calculate_tour_cost(tour)
    
    # Check if this tour has a lower cost than the current minimum
    if cost < min_cost:
        min_cost = cost
        optimal_tour = tour

print("Tour:", optimal_tour)
print("Total travel cost:", round(min_cost, 2))