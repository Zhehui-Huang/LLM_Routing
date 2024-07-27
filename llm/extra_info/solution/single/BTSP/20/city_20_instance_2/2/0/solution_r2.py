import math
from itertools import permutations

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_and_max_distance(tour, coordinates):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

def solve_tsp_brute_force(coordinates):
    n = len(coordinates)
    min_max_distance = float('inf')
    best_tour = None

    for perm in permutations(range(1, n)):
        current_tour = [0] + list(perm) + [0]
        total_cost, max_distance = total_and_max_distance(current_tour, coordinates)
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = current_tour

    total_cost, max_distance = total_and_max_distance(best_tour, coordinates)

    return best_tour, total_cost, max_distance

# Coordinates of each city including the depot
coordinates = [
    (3, 26),
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

best_tour, total_travel_cost, max_consecutive_distance = solve_tsp_brute_force(coordinates)

print("Tour:", best_tour)
print("Total travel cost:", total_travel_sum)
print("Maximum distance between consecutive cities:", max_consecutive_distance)