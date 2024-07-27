import itertools
import math

# Define cities' coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 2)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combinations of 3 cities excluding the depot
city_combinations = itertools.combinations(range(1, 20), 3)

min_cost = float('inf')
best_tour = None

# Evaluate each combination
for combination in city_combinations:
    full_tour = [0] + list(combination) + [0]
    
    # Generate all permutations of the 3 cities for the minimum tour calculation
    for perm in itertools.permutations(combination):
        # Add depot city
        current_tour = [0] + list(perm) + [0]
        # Calculate total travel cost
        current_cost = sum(euclidean_distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))

        # Update minimum cost and tour
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")