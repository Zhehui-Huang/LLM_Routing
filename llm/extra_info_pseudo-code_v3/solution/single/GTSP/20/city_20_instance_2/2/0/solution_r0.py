import itertools
import math

# Coordinates of cities with the depot city included
cities = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# Grouping of cities (0 is depot in separate group)
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Function to calculate Euclidean distance between two cities
def distance(index1, index2):
    x1, y1 = cities[index1]
    x2, y2 = cities[index2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generating all combinations of tours by taking one city from each group
combinations = list(itertools.product(*groups))
best_tour = None
min_cost = float('inf')

# Computing cost for each tour combination and comparing to find the minimum cost tour
for comb in combinations:
    tour = [0] + list(comb) + [0]
    cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Displaying the results
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))