import random
import math
from itertools import permutations

# Cities data
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

# City groups
city_groups = {
    0: [7, 10, 11, 12],
    1: [3, 8, 13, 16],
    2: [2, 4, 15, 18],
    3: [1, 9, 14, 19],
    4: [5, 6, 17]
}

def distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def calculate_tour_cost(tour):
    """ Calculate the total cost of a given tour. """
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i+1])
    return cost

def find_shortest_tour():
    """ Find the shortest possible tour starting and ending at depot, visiting one city from each group. """
    best_tour = None
    best_cost = float('inf')
    
    # Iterate through all possible combinations of cities (one from each group)
    for selection in permutations([random.choice(cities) for cities in city_groups.values()]):
        full_tour = [0] + list(selection) + [0]
        cost = calculate_tour_cost(full_tour)
        if cost < best_cost:
            best_tour, best_cost = full_tour, cost
    
    return best_tour, best_cost

# Perform the calculation
tour, total_cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)