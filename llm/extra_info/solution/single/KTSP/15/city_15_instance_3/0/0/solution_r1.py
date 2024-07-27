import itertools
import math

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


def compute_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def total_distance(tour):
    return sum(compute_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generate combinations of 9 other cities
other_cities = list(range(1, 15))  # city indices excluding the depot (0)
combinations = itertools.combinations(other_cities, 9)

min_distance = float('inf')
best_tour = None

# Explore each combination + depot as potential tour
for combo in combinations:
    # Prepare the tour permutation
    full_tour_candidates = [0] + list(combo) + [0]
    
    # Permute the internal cities (excluding the depot additions at start and end)
    for perm in itertools.permutations(full_tour_candidates[1:-1]):
        current_tour = [0] + list(perm) + [0]
        current_distance = total_distance(current_tour)
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = current_candidates

# Output the best tour and travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")