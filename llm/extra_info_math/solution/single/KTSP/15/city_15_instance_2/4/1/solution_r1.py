import math
from itertools import permutations

# Define functions to calculate the Euclidean distance between two cities
def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

# Define all cities with their coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Helper function to record tour distance
def tour_distance(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    return total_dist

# Calculate the shortest tour having exactly 8 cities, including the depot city (0)
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = []

    # Generate all combinations of additional 7 cities
    for cities_subset in combinations(cities.keys() - {0}, 7):
        all_tour_cities = [0] + list(cities_subset) + [0]

        # Generate all permutations of visiting cities in subset
        for tour_permutation in permutations(list(cities_subset)):
            candidate_tour = [0] + list(tour_permutation) + [0]
            current_distance = tour_distance(candidate_tour)

            # Update to find the minimum distance tour
            if current_distance < min_distance:
                min_distance = current_distance
                best_tour = candidate_tour

    return best_tour, min_distance

# Execute the function and capture the result
calculated_tour, calculated_cost = find_shortest_tour()

# Output the results
print("Tour:", calculated_tour)
print("Total travel cost:", calculated_cost)