import math
from itertools import permutations

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

# Determine all possible sets of 6 cities including city 0
city_indices = list(cities.keys())
possible_combinations = [
    (0,) + combo
    for combo in permutations(city_indices[1:], 5)
    if 0 in combo
]

# Function to calculate the total path cost for a given tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Generate possible tours that include city 0 at the start and end, considering only 6 cities
minimum_cost = float('inf')
best_tour = None

for combo in possible_combinations:
    extended_combo = combo + (0,)  # Ensure it returns to the depot
    # Generate all permutations of the 6 selected cities (keeping first and last city fixed as the depot)
    for perm in permutations(combo[1:-1]):
        current_tour = (combo[0],) + perm + (combo[-1],)
        current_cost = calculate_tour_cost(current_tour)
        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_tour = current_tour

# Output the optimum tour and its cost
print("Tour:", list(best_tour))
print("Total travel cost:", minimum_cost)