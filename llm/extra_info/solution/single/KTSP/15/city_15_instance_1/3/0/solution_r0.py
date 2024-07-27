import itertools
import math

# Coordinates of each city including the depot
coordinates = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57),
    6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        total_distance += euclidean_distance(coordinates[city_from], coordinates[city_to])
    return total_distance

# Main logic for finding shortest tour starting and ending at the depot that visits exactly 6 cities
all_cities = list(range(1, 15))
min_tour = None
min_cost = float('inf')

for cities_combination in itertools.combinations(all_cities, 5):
    full_cities_tour = [0] + list(cities_combination) + [0]
    for tour_permutation in itertools.permutations(full_cities_tour[1:-1]):
        current_tour = [0] + list(tour_permutation) + [0]
        current_cost = calculate_total_distance(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            min_tour = current_tour

# Display the outcome
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")