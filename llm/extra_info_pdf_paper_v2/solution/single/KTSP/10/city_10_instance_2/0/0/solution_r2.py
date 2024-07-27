import math
from itertools import combinations, permutations

# City coordinates {city_index: (x, y)}
cities = {
    0: (90, 3),
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

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Determine all possible sets of 6 cities including the depot city at index 0
city_indices = list(cities.keys())
possible_combinations = [
    (0,) + combo for combo in combinations(city_indices[1:], 5)
]

# Evaluate all possible tours for each combination
minimum_cost = float('inf')
best_tour = None

for combo in possible_combinations:
    # Generate all permutations of the 5 selected cities plus the depot city
    for perm in permutations(combo[1:]):
        tour = (0,) + perm + (0,)  # Start and end at the depot city
        cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        if cost < minimum_cost:
            minimum_cost = cost
            best_tour = tour

# Output the optimum tour and its cost
print("Tour:", list(best_tour))
print("Total travel cost:", round(minimum_cost, 2))