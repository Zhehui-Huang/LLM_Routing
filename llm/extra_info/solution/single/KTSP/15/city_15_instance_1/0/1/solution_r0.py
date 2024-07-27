import math
from itertools import permutations

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

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

min_cost = float('inf')
best_tour = None

# All possible city combinations to visit considering the robot visits exactly 6 cities (including the depot)
all_city_combinations = permutations(range(1, 15), 5)  # generate combinations from city 1 to 14 (5 cities + depot)

for cities_combo in all_city_combinations:
    current_tour = [0] + list(cities_combo) + [0]  # start and end at the depot city 0
    tour_cost = calculate_tour_cost(current_tour)
    if tour_cost < min_cost:
        min_cost = tour_cost
        best_tour = current_tour

# Printing the solution
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")