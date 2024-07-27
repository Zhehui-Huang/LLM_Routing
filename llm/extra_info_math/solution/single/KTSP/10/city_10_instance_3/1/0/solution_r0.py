import itertools
from scipy.spatial.distance import euclidean
import numpy as np

# Given coordinates of the cities
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

def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i+1])
    return total_distance

# Generate all combinations consisting of 6 other cities plus the depot (0)
city_indices = list(cities.keys())[1:]  # Exclude the depot city from the combinations
combinations = itertools.combinations(city_indices, 6)  # Choose 6 cities because depot is always included

best_tour = None
best_cost = float('inf')

# Explore each combination, including the depot city
for combo in combinations:
    full_set = [0] + list(combo)
    # Generate all permutations of the selected cities to explore possible tours
    for perm in itertools.permutations(full_set):
        if perm[0] == 0:  # Ensure the tour starts and ends at the depot
            tour = list(perm) + [0]
            cost = evaluate_tour(tour)
            if cost < best_cost:
                best_cost = cost
                best_tour = tour

# Output the best tour found and its total cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")