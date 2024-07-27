import itertools
import math
from sys import float_info

# City coordinates
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

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_distance(tour):
    """ Calculate the total distance of the given tour """
    return sum([euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)])

# The goal here is to select 7 additional cities besides the depot (total 8 cities including the depot city)
min_distance = float_info.max
best_tour = None

# Iterate over all combinations of 7 cities chosen from the remaining 14 (excluding the depot)
for cities_subset in itertools.combinations(range(1, 15), 7):
    current_cities = [0] + list(cities_subset)
    
    # Iterate over all permutations of the chosen cities to find the minimum distance path
    for permutation in itertools.permutations(current_cities[1:]):
        tour = [0] + list(permutation) + [0]
        current_distance = calculate_total_distance(tour)
        
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = tour

# Return the best tour and its total distance
print("Tour:", best_tour)
print("Total travel cost:", min_distance)