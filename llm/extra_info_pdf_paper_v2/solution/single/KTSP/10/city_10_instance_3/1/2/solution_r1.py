import math
from itertools import permutations

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(tour[i-1], tour[i])
    return total_cost

# Generate all combinations of 6 cities (excluding the depot 0)
city_combinations = combinations([i for i in range(1, 10)], 6)

min_cost = float('inf')
best_tour = None

# Explore all combinations and permutations of tours
for combination in city_combinations:
    for perm in permutations(combination):
        # Create a tour starting and ending at the depot city 0
        tour = [0] + list(perm) + [0]
        cost = calculate_tour_cost(tour)
        # Check if the found tour has a lower cost
        if cost < minck] Cost: {min_cost}')