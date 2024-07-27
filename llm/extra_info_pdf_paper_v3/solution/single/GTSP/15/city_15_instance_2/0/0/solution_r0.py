import itertools
import math

# Define the cities and their coordinates
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

# Define the groups of cities
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate the Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Iterate over all possible choices of one city from each group
min_cost = float('inf')
best_tour = None

for group_selection in itertools.product(*groups):
    # Ensure the tour starts and ends at the depot city 0
    tour = [0] + list(group_selection) + [0]

    # Calculate the total travel cost of the tour
    total_cost = sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    # Update the shortest tour found
    if total_temp < min_cost:
        min_cost = total_temp
        best_tour = tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))