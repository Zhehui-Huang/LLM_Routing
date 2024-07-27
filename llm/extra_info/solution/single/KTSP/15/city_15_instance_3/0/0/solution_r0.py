import itertools
import math
from scipy.spatial import distance_matrix

# Define the coordinates of the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Compute the Euclidean distance matrix
coords = list(cities.values())
dist_matrix = distance_matrix(coords, coords)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += dist_matrix[tour[i], tour[i + 1]]
    return total_distance

# Generate all combinations of 9 cities apart from the depot city 0
city_indices = list(cities.keys())
city_indices.remove(0)
combinations = itertools.combinations(city_indices, 9)

# Find the best subset of cities and shortest tour for 10 cities including the depot
min_distance = float('inf')
best_tour = None

for combo in combinations:
    current_cities = [0] + list(combo)
    # Generate permutations of the city order for the current combination
    for tour in itertools.permutations(current_cities):
        if tour[0] == 0 and tour[-1] == 0:  # Ensure tour starts and ends at the depot city 0
            current_distance = calculate_total_distance(tour)
            if current_distance < min_distance:
                min_distance = current_distance
                best_tour = tour

# Output the best tour and travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance}")