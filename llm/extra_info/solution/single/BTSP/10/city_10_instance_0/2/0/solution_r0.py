import math
from itertools import permutations

# Given coordinates for the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance
def calc_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate all possible tours starting and ending at the depot
def generate_tours():
    cities_without_depot = list(cities.keys())[1:]
    for city_order in permutations(cities_without_depot):
        tour = [0] + list(city_order) + [0]
        yield tour

# Calculate distance metrics for the given tour
def tour_metrics(tour):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calc_distance(cities[tour[i]], cities[tour[i + 1]])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance
    return total_distance, max_distance

# Find the optimal tour minimizing the longest distance between consecutive cities
def find_optimal_tour():
    minimum_max_distance = float('inf')
    optimal_tour = None
    optimal_total_distance = 0

    for tour in generate_tours():
        total_distance, max_distance = tour_metrics(tour)
        if max_distance < minimum_max_distance:
            minimum_max_disance = max_distance
            optimal_tour = tour
            optimal_total_distance = total_distance

    return optimal_tour, optimal_total_distance, minimum_max_disance

# Execute to get the required results
optimal_tour, optimal_total_distance, optimal_max_distance = find_optimal_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {optimal_max_distance:.2f}")