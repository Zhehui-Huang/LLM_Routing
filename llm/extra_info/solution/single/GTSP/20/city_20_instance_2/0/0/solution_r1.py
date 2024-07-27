import math
from itertools import product

# Coordinates of the depot and cities
locations = [
    (3, 26),   # Depot 0
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
    (30, 48),  # City 19
]

# Group of city indices
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

def euclidean_dist(i, j):
    return math.sqrt((locations[i][0] - locations[j][0]) ** 2 + (locations[i][1] - locations[j][1]) ** 2)

# Calculate all potential combinations of cities, one from each group
def all_possible_tours(groups):
    return product(*groups)

# Calculate tour length
def tour_length(tour):
    total_length = euclidean_dist(0, tour[0])  # From depot to first city in tour
    for i in range(1, len(tour)):
        total_length += euclidean_dist(tour[i-1], tour[i])  # From each city to next
    total_length += euclidean_dist(tour[-1], 0)  # Back to depot
    return total_length

# Evaluate minimum tour
min_cost = float('inf')
min_tour = []

for tour in all_possible_tours(groups):
    cost = tour_length(tour)
    if cost < min_cost:
        min_cost = cost
        min_tour = [0] + list(tour) + [0]

# Output
print("Tour:", min_tour)
print("Total travel cost: {:.2f}".format(min_cost))