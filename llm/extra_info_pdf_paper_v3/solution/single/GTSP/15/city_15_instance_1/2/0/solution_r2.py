import math
from itertools import product, permutations

def euclidean_distance(city1, city2):
    """
    Calculate the Euclidean distance between two city coordinates.
    """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Define city coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Define groups of cities
groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

def generate_possible_combinations(groups):
    """
    Generates all combinations by picking one city from each group.
    """
    return product(*[groups[i] for i in sorted(groups.keys())])

def calculate_total_cost(tour):
    """
    Calculates the total cost of a given tour.
    """
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def find_best_tour(groups):
    """
    Finds the tour with the minimum distance.
    """
    best_tour = None
    minimum_cost = float('inf')
    
    for combination in generate_possible_combinations(groups):
        tour = [0] + list(combination) + [0]
        cost = calculate_total_cost(tour)
        if cost < minimum_no
    return best_tour, minimum_cost

# Calculating the shortest tour and its cost
best_tour, min_cost = find_best_tour(groups)

# Outputting the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")