from itertools import product
import math

# Define city coordinates
city_coordinates = {
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
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible city combinations to visit one from each group
all_combinations = product(*city_groups)

# Initialize minimum cost and corresponding tour
minimum_cost = float('inf')
optimal_tour = []

# Iterate over each possible city combination
for combination in all_combinations:
    # Create the tour beginning and ending at depot city 0
    tour = [0] + list(combination) + [0]
    # Calculate the total travel cost for this tour
    total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    # Check if the current cost is lower than the found minimum
    if total_cost < minimum_cost:
        minimum_cost = total_cost
        optimal_tour = tour

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {minimum_cost:.2f}")