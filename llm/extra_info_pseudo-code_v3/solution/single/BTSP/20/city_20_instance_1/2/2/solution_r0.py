import math
from itertools import permutations

# Data Input
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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all possible permutations of the cities (excluding the depot)
city_indices = list(cities.keys())[1:]  # Excluding depot initially for permutations
all_tours = permutations(city_indices)

# Evaluate each tour based on the maximum distance the robot travels between two consecutive cities
best_max_distance = float('inf')
best_tour = None

for tour in all_tours:
    tour_with_depot = (0,) + tour + (0,)
    max_dist_between_cities = max(distance(tour_with_depot[i], tour_with_depot[i+1]) for i in range(len(tour_with_depot) - 1))

    if max_dist_between_cities < best_max_distance:
        best_max_distance = max_dist_between_cities
        best_tour = tour_with_depot

# Calculate total travel cost of the best found tour
total_travel_cost = sum(distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))

# Output in the required format
print("Tour:", list(best_tour))
print("Total travel cost:", round(total_travel_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))