import math
from itertools import product

# Define the coordinates of the cities
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Define the groups
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

def euclidean_distance(a, b):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_tour_cost(tour):
    """ Calculate the total tour cost based on Euclidean distance. """
    cost = 0
    for i in range(len(tour)-1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def find_best_tour():
    # Generate all possible tours by picking one city from each group and calculating the total distance
    min_cost = float('inf')
    best_tour = None

    for combination in product(*groups):
        tour = [0] + list(combination) + [0]
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

    return best_tour, min_cost

# Find the optimal tour and the corresponding cost
best_tour, best_cost = find_best_tour()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)