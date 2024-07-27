import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates
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

# Group members
groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Generates all possible selections of cities, one from each group
def generate_possible_combinations(groups):
    all_combinations = []
    for combo in permutations(groups):
        cart_product = [[(group_index, city) for city in groups[group_index]] for group_index in combo]
        for product in itertools.product(*cart_product):
            all_combinations.append([item[1] for item in product])
    return all_combinations

# Calculate tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

# Find the best tour
def find_best_tour(groups):
    min_cost = float('inf')
    best_tour = None
    for comb in generate_possible_combinations(groups):
        tour_candidates = [0] + comb + [0]
        current_cost = calculate_tour_cost(tour_candidates)
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = tour_candidates
    return best_tour, min_cost

# Compute the result
best_tour, total_cost = find_best_tour(groups)

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")