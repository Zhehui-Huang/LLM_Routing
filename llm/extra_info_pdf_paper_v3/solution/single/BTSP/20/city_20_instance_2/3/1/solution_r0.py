import math
from itertools import permutations

# City coordinates
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

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_max_and_total_distance(tour):
    max_distance = 0
    total_distance = 0
    previous_city = tour[0]
    
    for current_city in tour[1:]:
        distance = euclidean_distance(cities[previous_city], cities[current_city])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance
        previous_city = current_city
    
    return total_distance, max_distance

# Creating initial tour starting and ending at the depot (city 0)
initial_tour = [0] + list(range(1, len(cities))) + [0]

# Calculate initial distances
total_distance, max_distance = calculate_max_and_total_distance(initial_tour)

# Improve tour by trying all permutations of the middle cities
best_tour = initial_tour[:]
best_max_distance = max_distance
best_total_distance = total_distance

# It is impractical to check all permutations for 20 cities, so here we use heuristic or simpler exhaustive attempts.
# We will use permutations but only on a subset of cities due to computational limitations.
# Since permutation of all cities is an N! problem, limit to a smaller number like 8 cities at a time.

for perm_indices in permutations(range(1, 9)):  # Only permute first 8 non-depot cities
    new_tour = [0] + list(perm_indices) + list(range(9, 20)) + [0]
    total_distance, max_distance = calculate_max_and_total_distance(new_tour)
    if max_distance < best_max_distance:
        best_tour = new_tour
        best_max_distance = max_distance
        best_total_distance = total_distance

# Display best possible solution found
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_distance}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")