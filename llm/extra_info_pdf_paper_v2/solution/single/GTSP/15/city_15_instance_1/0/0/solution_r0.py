import math
from itertools import permutations

# City coordinates (ID, x, y)
city_coords = {
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

# City groups
city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

def euclidean_distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generates all possible city selections (one from each group)
def city_selections(groups):
    if not groups:
        return [[]]
    first_group = groups[0]
    rest_groups = groups[1:]
    rest_selections = city_selections(rest_groups)
    selections = []
    for city in first_group:
        for selection in rest_selections:
            selections.append([city] + selection)
    return selections

# Calculate the shortest tour from the depot, visiting one city per group, and returning
def find_shortest_tour():
    all_selections = city_selections(city_groups)
    best_tour = None
    min_cost = float('inf')
    for selection in all_selections:
        # Consider all permutations of the selected cities
        for permutation in permutations(selection):
            tour = [0] + list(permutation) + [0]
            cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            if cost < min_cost:
                min_cost = cost
                best_tour = tour
    return best_tour, min_cost

# Calculate and print the optimal tour and cost
tour, cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))