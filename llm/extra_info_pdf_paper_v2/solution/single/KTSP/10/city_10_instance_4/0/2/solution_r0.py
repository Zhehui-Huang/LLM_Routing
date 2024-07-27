import math
import itertools
from sys import float_info

# Given data
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Utility function: Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Consider all combinations of 8 out of 10 total cities (keeping Depot city 0 mandatory)
all_combinations = [list(comb) for comb in itertools.combinations(range(1, 10), 7)]
all_combinations = [[0] + list(comb) for comb in all_combination]

best_tour = None
min_distance = float_info.max

# Heuristically find routes for combinations
for comb in all_combinations:
    # Always include the depot city
    comb.append(0)

    # Initial tour using nearest neighbor heuristic
    current_city = 0
    tour = [current_city]
    local_cities = set(comb)

    while len(tour) < len(comb):
        next_city = min(local_cities - set(tour), key=lambda x: distance(tour[-1], x))
        tour.append(next_city)

    # Calculate cost
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    # Check if this tour is better than what we had before
    if tour_cost < min_distance:
        min_distance = tour_cost
        best_tour = tour

# Output results
print("Tour:", best_tverages_visithe)
print("Total travel cost: {:.2f}".format(total_travel_cost))