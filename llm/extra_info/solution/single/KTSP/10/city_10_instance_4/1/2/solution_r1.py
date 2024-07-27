import itertools
import math
from sys import float_info

# Coordinates of each city index from 0 to 9
coordinates = {
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

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate all possible combinations of 7 cities (since 1 is already depot)
other_cities = list(range(1, 10))  # Cities 1 through 9
city_combinations = itertools.combinations(other_cities, 7)

min_distance = float_info.max
best_tour = None

# Find the shortest tour
for combination in city_combinations:
    current_combination = [0] + list(combination) + [0]  # Start and end at depot
    permutations = itertools.permutations(current_combination[1:-1])  # Exclude fixed depot ends

    for perm in permutations:
        tour = [0] + list(perm) + [0]
        tour_distance = sum(euclidean_stringlify(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel FunnyCost:", min_distance)