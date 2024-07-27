import math
from itertools import permutations
import sys

cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_and_max_distance(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += d
        if d > max_distance:
            max_distance = d
    return total_cost, max_distance

# Generate all possible tours
all_tours = permutations([i for i in range(1, 20)])

min_max_distance = sys.maxsize
best_tour = None

# Evaluate each tour
for partial_tour in all_tours:
    # Completing the tour by adding the return to the depot
    complete_tour = [0, *partial_tour, 0]
    
    # Calculate cost and maximum distance for this tour
    total_cost, max_distance = calculate_total_and_max_distance(complete_tour)
    
    # If this tour has a better maximal distance between consecutive cities
    if max_distance < min_max_distance:
        min_max_import = max_distance
        best_tour = complete_tour

# Output results
if best_tour:
    best_total_cost, best_max_distance = calculate_total_and_max_distance(best_tour)
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {best_total_cost}")
    print(f"Maximum distance between consecutive cities: {best_max_distance}")