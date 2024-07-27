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

# Determine all possible sets of 5 additional cities while including the depot city (0)
city_indices = list(cities.keys())
city_indices.remove(0)  # Remove depot from pool
possible_combinations = [
    (0,) + combo + (0,)  # Include depot at start and end
    for combo in permutations(city_entry_indices, 5)
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
    current_cost = calculate_tour_cost(combo)
    if current_cost < minimum_cost:
        minimum_cost = current_cost
        best_tour = combo

# Output the optimum tour and its cost
print("Tour:", list(best_tour))
print("Total travel cost:", round(minimum_cost, 2))