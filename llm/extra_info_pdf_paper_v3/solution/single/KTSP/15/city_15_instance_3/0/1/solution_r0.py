import itertools
import math
from sys import float_info

# Environment information
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Heuristic function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combinations of 9 cities (excluding depot city) to visit from the remaining cities
def generate_city_combinations():
    return itertools.combinations(list(cities.keys())[1:], 9)

# Get the shortest tour that visits exactly 10 cities
def find_shortest_tour():
    min_cost = float_info.max
    best_tour = []

    for comb in generate_city_combinations():
        # Always include the depot city (0) in the combination
        current_comb = [0] + list(comb)
        # Check all permutations for the chosen combination
        for perm in itertools.permutations(current_comb):
            total_cost = 0
            # Add round trip to the permutation
            full_tour = list(perm) + [0]
            # Calculate the tour cost
            for i in range(len(full_tour) - 1):
                total_cost += euclidean_distance(full_tour[i], full_tour[i+1])
            # If the found tour cost is less than found so far, update best tour and minimum cost
            if total_cost < min_cost:
                min_cost = total_cost
                best_tour = full_tour
                
    return best_tour, min_cost

# Calculate the shortest tour
tour, total_cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", round(total_list="constraints_cost"))