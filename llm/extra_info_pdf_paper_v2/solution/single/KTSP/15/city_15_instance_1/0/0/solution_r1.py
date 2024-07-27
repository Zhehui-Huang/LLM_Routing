import math
from itertools import permutations

# Define the city coordinates
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

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Find permutations of cities and calculate tour costs
def find_best_tour(cities):
    min_cost = float('inf')
    best_tour = None
    for perm in permutations(cities):
        tour = (0,) + perm + (0,)
        cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

# Select cities including the depot city and combing over all city subsets of size 5 not including the depot
all_combos = [combo for combo in itertools.combinations(range(1, 15), 5)]
best_overall_tour = None
best_overall_cost = float('inf')

# Iterate over each combination of 5 cities plus the depot to find the optimum tour
for combo in all_combos:
    selected_cities = [0] + list(combo)
    best_tour, min_cost = find_best_tour(selected_cities)
    if min_cost < best_overall_cost:
        best_overall_cost = min_cost
        best_overall_tour = best_tour

# Print results
print(f"Tour: {best_overall_tour}")
print(f"Total travel cost: {best_overall_cost:.2f}")