import math
from itertools import permutations

# Coordinates of the cities indexed from 0
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

# Euclidean distance calculator
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

def find_optimal_tour():
    num_cities = len(cities)
    
    # Brute-force find: generate all permutations
    # Iterating through all except the first (depot)
    all_tours = permutations(range(1, num_cities))
    min_max_distance = float('inf')
    best_tour = None

    # Evaluate each possible tour
    for tour in all_tours:
        full_tour = [0] + list(tour) + [0]  # start and return to the depot
        max_distance_in_tour = max(
            euclidean_distance(full_tour[i], full_tour[i + 1]) for i in range(len(full_tour) - 1)
        )
        if max_distance_in_tour < min_max_distance:
            min_max_distance = max_distance_in_tour
            best_tour = full_tour
    
    # Calculate total cost of the best tour found
    if best_tour:
        total_distance = sum(
            euclidean_distance(best_tour[i], best_tour[i + 1]) for i in range(len(best_tour) - 1)
        )
        return best_tour, total_distance, min_max_distance
    
    return None, None, None

# Find and print the optimal tour
optimal_tour, total_travel_cost, max_distance = find_optimal_tour()

if optimal_tour:
    print("Tour:", optimal_tour)
    print("Total travel cost:", total_travel_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No valid tour found.")