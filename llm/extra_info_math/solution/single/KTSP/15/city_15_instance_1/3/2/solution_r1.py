import itertools
import math

# Given cities coordinates.
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

# Calculate Euclidean distance.
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible 5-city combinations (excluding the depot city).
city_combinations = itertools.combinations(range(1, 15), 5)

# Variable to keep the minimum distance tour and its cost.
min_tour_cost = float('inf')
min_tour = None

# Evaluate each combination.
for combo in city_combinations:
    full_combo = [0] + list(combo) + [0]  # start and end at the depot city 0
    # Permute the middle cities to find the shortest path.
    for perm in itertools.permutations(combo):
        current_tour = [0] + list(perm) + [0]
        # Calculate the total tour cost.
        tour_cost = sum(distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
        # Check if this tour has a new minimum cost.
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
            min_tour = current_tour

# Display result
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_tour_cost}")