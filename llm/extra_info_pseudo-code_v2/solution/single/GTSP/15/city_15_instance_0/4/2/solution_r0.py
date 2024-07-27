import math
import random
from itertools import permutations

# Input data
positions = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((positions[city1][0] - positions[city2][0]) ** 2 + (positions[city1][1] - positions[city2][1]) ** 2)

# Generate all possible tours by selecting one city per group and calculate costs
def find_minimum_tour():
    min_cost = float('inf')
    best_tour = []

    for combination in permutations(groups):
        for cities in cartesian_product(*combination):
            tour = [0] + list(cities) + [0]
            cost = calculate_tour_cost(tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = tour

    return best_tour, min_cost

def cartesian_product(*sequences):
    if not sequences:
        return iter([[]])
    else:
        return (items + [item] for items in cartesian_product(*sequences[:-1]) for item in sequences[-1])

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i + 1])
    return cost

# Usage of the function
best_tour, total_cost = find_minimum_tour()

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")