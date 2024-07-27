import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates for each city including the depot (0 index)
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

def calculate_tour_cost_and_max_distance(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += distance
        max_distance = max(max_distance, distance)
    return total_cost, max_distance

def find_optimal_tour():
    num_cities = len(cities)
    best_tour = None
    min_max_distance = float('inf')
    for perm in permutations(range(1, num_cities)):
        current_tour = [0] + list(perm) + [0]
        _, max_dist = calculate_tour_cost_and_max_distance(current_tour)
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_tour = current_tour
    total_cost, max_distance = calculate_tour_cost_and_max_distance(best_tour)
    return best_tour, total_cost, max_distance

# Let's run the function and output the results.
tour, total_cost, max_distance = find_optimal_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between any two consecutive cities: {max_distance:.2f}")