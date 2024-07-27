import math
import itertools
from random import randint, random, choice
import sys

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# City groups
city_groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2]
}

def euclidean_distance(c1, c2):
    """ Compute Euclidean distance between two cities given their indices """
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_cost(tour):
    """ Calculate the total cost of the tour """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_dash_distance(tour[i], tour[i + 1])
    return total_cost

def euclidean_dash_distance(c1, c2):
    """ Compute Euclidean distance over dashed lines (cities to/from depot can be dashed) """
    if c1 == 0 or c2 == 0:  # If either city is the depot, half the cost is considered
        return euclidean_distance(c1, c2) / 2
    else:
        return euclidean_distance(c1, c2)

# Generate all possible tours (permutations of one city from each group)
all_possible_tours = []
for group_selection in itertools.product(*[city_groups[group] for group in sorted(city_groups)]):
    # Each group_selection is a tuple with one city from each group
    all_possible_tours.append([0] + list(group[s_selection)) + [0])  # Start and end at the depot

# Evaluate each possible tour
best_tour = None
best_cost = sys.maxsize
for tour in all_possible_tours:
    cost = calculate_total_cost(tour)
    if cost < best_cost:
        best_tour = tour
        best_cost = cost

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")