import itertools
import math

# Defined cities with their coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all combinations of 6 non-depot cities
city_indices = list(cities.keys())[1:]  # Exclude depot
all_combinations = itertools.combinations(city_indices, 6)

# Keep track of the shortest path found
shortest_dist = float('inf')
shortest_path = []

# Evaluate each combination by creating possible tours using permutations including the depot
for combination in all_combinations:
    # Add depot to the current combination and evaluate each permutation
    current_cities = (0,) + combination
    for perm in itertools.permutations(current_cities):
        # Ensure to start and end at depot
        if perm[0] == 0 and perm[-1] == 0:
            # Calculate distance for this specific tour permutation
            tour_distance = sum(calculate_distance(cities[perm[i]], cities[perm[i + 1]]) for i in range(len(perm) - 1))
            # Check if this tour is the shortest one found so far
            if tour_distance < shortest_dist:
                shortest_dist = tour_distance
                shortest_path = list(perm)

# Output the result
print(f'Tour: {shortest_path}')
print(f'Total travel cost: {shortest_dist}')