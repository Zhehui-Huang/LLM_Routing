import math
import itertools

# Coordinates for each city including the depot
cities = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Euclidean distance calculation function
def distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Generator for all tours starting and ending at the depot city and visiting others exactly once
def all_possible_tours():
    for perm in itertools.permutations(list(range(1, len(cities)))):
        yield [0] + list(perm) + [0]

# Initialize the search for the minimum
min_max_distance = float('inf')
best_tour = None
total_cost = 0

# Test all potential tours
for tour in all_possible_tours():
    max_distance_in_tour = max(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    tour_cost = sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    if max_distance_in_tour < min_max_distance:
        min_max_distance = max_distance_in_tour
        best_tour = tour
        total_cost = tour_cost

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_maxic_distance:.2f}")