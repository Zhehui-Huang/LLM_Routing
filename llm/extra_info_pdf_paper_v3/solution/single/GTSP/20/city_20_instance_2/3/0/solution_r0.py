import math

# Step 0: City coordinates and group definition
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

groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Step 1: Define a function to calculate Euclidean distance between two cities
def calc_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Step 2: Implementing a solver to find the best city from each group to form the shortest path
from itertools import permutations

def find_shortest_tour():
    min_cost = float('inf')
    best_tour = None
    
    # Consider all permutations of one representative from each group
    for chosen_cities in permutations([min(group, key=lambda x: calc_distance(0, x)) for group in groups]):
        tour_cost = calc_distance(0, chosen_cities[0])
        for i in range(len(chosen_cities) - 1):
            tour_cost += calc_distance(chosen_cities[i], chosen_cities[i + 1])
        tour_cost += calc_distance(chosen_cities[-1], 0)

        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = [0] + list(chosen_cities) + [0]
    
    return best_tour, min_cost

# Step 3: Calculate the tour and its total cost
tour, total_cost = find_shortest_tour()

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")