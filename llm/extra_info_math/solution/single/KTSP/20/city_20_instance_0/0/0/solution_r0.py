import itertools
import math

# Coordinates of the cities
cities = [
    (8, 11),  # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of 3 additional cities as we always include the depot city 0
city_combinations = itertools.combinations(range(1, 20), 3)

# Variables to hold minimum distance and best tour
min_distance = float('inf')
min_tour = None

# Loop through combinations to determine the shortest tour
for combo in city_combinations:
    tour_candidates = [0] + list(combo) + [0]  # Creating the tour including depot 0 at start and end
    # Generate all permutations of the 3 cities to ensure we get the minimum tour cost
    for perm in itertools.permutations(tour_candidates[1:-1]):
        full_tour = [0] + list(perm) + [0]
        # Calculate the total travel cost
        total_cost = sum(calc_distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour) - 1))
        # Check if this permutation gives a shorter tour
        if total_cost < min_distance:
            min_distance = total_cost
            min_tour = full_tour

# Results
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_distance:.2f}")