import math
from itertools import permutations

# Coordinates of cities
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Groups
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

# Calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Calculate the travel cost of a given tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Find the shortest tour that visits one city from each group
def find_shortest_tour():
    all_group_permutations = list(permutations(groups))
    best_tour = None
    best_cost = float('inf')

    # Try every permutation of group selections
    for group_order in all_group_permutations:
        # Generate all possible selectings one city from each group
        for city_selection in itertools.product(*group_order):
            current_tour = [0] + list(city_selection) + [0]
            current_cost = calculate_tour_cost(current_tour)
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = current_tour
                
    return best_tour, best_cost

# Solving the problem
tour, total_cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)