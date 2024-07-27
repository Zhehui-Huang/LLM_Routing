import math
from itertools import permutations

# Coordinates of the cities (city index: (x, y))
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

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Finding the optimal tour that minimizes the maximum leg distance
def find_optimal_tour():
    min_max_distance = float('inf')
    best_tour = []
    best_total_distance = 0

    # Generate all permutations of cities excluding the depot city 0
    for perm in permutations(cities.keys() - {0}):
        tour = [0] + list(perm) + [0]
        total_distance = 0
        max_leg_distance = 0
        for i in range(len(tour) - 1):
            dist = calculate_distance(tour[i], tour[i+1])
            total_distance += dist
            if dist > max_leg_distance:
                max_leg_distance = dist

        # Update best tour if current max leg distance is smaller
        if max_leg_distance < min_max_distance:
            min_max_distance = max_leg_distance
            best_tour = tour
            best_total_distance = total_distance

    return best_tour, best_total_distance, min_max_distance

# Extract tour details
optimal_tour, total_travel_cost, max_distance_between_cities = find_optimal_tour()

# Print the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance_between_cities:.2f}")