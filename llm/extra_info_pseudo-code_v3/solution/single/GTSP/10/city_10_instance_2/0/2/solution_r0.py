import itertools
import math
from sys import float_info

# Define the cities and their coordinates
cities = {
    0: (90, 3),   # depot
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Define city groups
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_distance(tour):
    """ Calculate the total travel cost for a given tour """
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

def find_shortest_tour():
    """ Find the shortest tour visiting one city from each group """
    shortest_tour = None
    minimum_distance = float_info.max

    # Try all permutations of one city from each group
    for combination in itertools.product(*city_groups):
        current_tour = [0] + list(combination) + [0]
        current_distance = calculate_total_distance(current_tour)
        if current_distance < minimum_distance:
            minimum_distance = current_distance
            shortest_tour = current_tour

    return shortest_tour, minimum_distance

# Find the shortest tour and its distance
shortest_tour, min_distance = find_shortest_tour()

# Print the results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {min_distance}")