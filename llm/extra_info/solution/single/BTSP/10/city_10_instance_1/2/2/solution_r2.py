import math
from itertools import permutations

# Define the cities' coordinates
coordinates = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible tours starting and ending at the depot city 0
def generate_tours():
    middle_cities = list(coordinates.keys())
    middle_cities.remove(0)
    for perm in permutations(middle_cities):
        yield [0] + list(perm) + [0]

# Function to find the optimal tour minimizing the longest jump between consecutive cities
def find_optimal_tour():
    min_max_distance = float('inf')
    optimal_tour = None
    tour_cost = float('inf')
    for tour in generate_tours():
        tour_distances = [distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)]
        max_dist = max(tour_distances)
        current_cost = sum(tour_distances)
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            optimal_tour = tour
            tour_cost = current_cost
    return optimal_tour, tour_cost, min_max_distance

# Compute the optimal tour
optimal_tour, tour_cost, min_max_distance = find_optimal_tour()

# Output results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {tour_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")