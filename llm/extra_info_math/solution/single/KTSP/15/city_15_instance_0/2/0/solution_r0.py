import itertools
import math

# Cities coordinates with depot as index 0
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate all combinations of 3 cities excluding the depot (city 0)
city_combinations = itertools.combinations(range(1, 15), 3)

min_cost = float('inf')
best_tour = None

# Testing all combinations
for comb in city_combinations:
    cities_in_tour = [0] + list(comb) + [0]  # Start and End at depot city 0

    # Calculate total tour cost for current combination
    tour_cost = sum(euclidean_distance(cities[cities_in_tour[i]], cities[cities_in_tour[i + 1]]) for i in range(len(cities_in_tour) - 1))
    
    # Update minimum cost and best tour found
    if tour_cost < min_cost:
        min_cost = tour_cost
        best_tour = cities_in_tour

# Output the best tour found and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")