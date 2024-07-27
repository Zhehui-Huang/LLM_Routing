import math
from itertools import permutations

# Coordinates for each city where the key is the city index
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

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all tours starting and ending at city 0
def generate_tours():
    city_indices = list(cities.keys())
    perms = permutations(city_indices[1:])
    return [[0] + list(perm) + [0] for perm in perms]

# Find tour with minimum maximum distance between consecutive cities
def find_best_tour(tours):
    min_max_distance = float('inf')
    best_tour = None

    for tour in tours:
        max_distance = max(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour

    # Calculate the total cost of the best tour
    total_cost = sum(calc_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))
    return best_tour, total_cost, min_max_distance

# Generate all possible tours
tours = generate_tours()

# Determine the tour with the optimal maximum segment length
best_tour, total_cost, min_max_distance = find_best_tour(tours)

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")