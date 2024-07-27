import math
from itertools import permutations, combinations

# Defining city coordinates
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

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to find the best tour among permutations
def find_best_tour(cities):
    min_cost = float('inf')
    best_tour = None
    for perm in permutations(cities):
        # Ensuring the tour starts and ends at the depot city 0
        tour = (0,) + perm + (0,)
        cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

# Evaluating all combinations of 5 cities, excluding the depot
all_city_indices = list(cities.keys())[1:]  # excluding the depot city index 0
all_combos = list(combinations(all_city_indices, 5))
best_overall_tour = None
best_overall_cost = float('inf')

# Iterate each combination of 5 cities adding the depot city 0
for combo in all_combos:
    selected_cities = combo
    best_tour, min_cost = find_best_tour(selected_cities)
    if min_cost < best_overall_cost:
        best_overall_cost = min_cost
        best_overal_tour = best_tour

# Print output
print(f"Tour: {best_overall_tour}")
print(f"Total travel cost: {best_overall_cost:.2f}")