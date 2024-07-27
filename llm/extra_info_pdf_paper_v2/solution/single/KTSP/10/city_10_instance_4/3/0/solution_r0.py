import itertools
import numpy as np
import math

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26),
    4: (92, 9), 5: (83, 61), 6: (22, 21), 7: (97, 70),
    8: (20, 99), 9: (66, 62)
}

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible 8-city tours starting and ending at depot (city 0)
def generate_tours():
    min_distance = float('inf')
    best_tour = None
    non_depot_cities = list(cities.keys())[1:]  # non-depot cities are 1 through 9
    city_combinations = itertools.combinations(non_depot_cities, 7)  # choose 7 to accompany city 0

    for subset in city_combinations:
        current_tour = [0] + list(subset) + [0]
        all_tours = itertools.permutations(current_tour[1:-1])  # permute only the inner cities

        for perm in all_tours:
            tour = [0] + list(perm) + [0]
            tour_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
            if tour_distance < min_distance:
                min_distance = tour_distance
                best_tour = tour

    return best_tour, min_distance

# Finding the best tour and the minimal travel cost
best_tour, minimal_travel_cost = generate_tours()

# Output result
print("Tour:", best_tour)
print("Total travel cost:", round(minimal_travelparam_cost, 2))