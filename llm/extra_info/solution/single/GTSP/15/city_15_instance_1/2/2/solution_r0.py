import math

# City coordinates as tuples
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

# City groups as defined
groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their indexes"""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

import itertools

# Consider all combinations of one city from each group (Cartesian Product)
min_cost = float('inf')
best_tour = None

for perm in itertools.product(groups[0], groups[1], groups[2], groups[3]):
    # Start tour at the depot, go through each city in the permutation, and return to the depot
    tour = [0] + list(perm) + [0]
    # Calculating tour cost
    current_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = tour

# Provide the output as requested
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(min_cost, 2)}")