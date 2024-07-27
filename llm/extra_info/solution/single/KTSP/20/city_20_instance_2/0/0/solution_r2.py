import itertools
import math
from sys import float_info

# Coordinates dictionary for 20 cities including a depot
cities = [
    (3, 26),   # City 0 (Depot)
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

# Calculating the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# To store smallest found distance and corresponding tour
min_distance = float_info.max
best_tour = []

# Consider all combos of 9 cities from the list (excluding depot)
for combo in itertools.combinations(range(1, 20), 9):
    # Check each permutation of the current combo of cities
    for perm in itertools.permutations(combo):
        # Complete tour with depot at start and end
        tour = [0] + list(perm) + [0]
        # Calculate total distance of completed tour
        tour_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        # Store the tour and distance if it's the shortest found
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost: {:.2f}".format(min_distance))