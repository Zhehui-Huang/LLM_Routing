import math
from itertools import permutations

# Coordinates of each city indexed by the city number
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to find the best tour with the smallest maximum distance between consecutive cities
def find_bottleneck_tsp_tour():
    n = len(cities)
    best_max_distance = float('inf')
    best_tour = None

    # Explore all permutations of cities (excluding the depot city at 0)
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if max_distance < best_max_distance:
            best_max_distance = max_distance
            best_tour = tour

    # Calculate the total distance of the best tour
    total_travel_cost = sum(distance(best_tour[i], best_tour[i + 1]) for i in range(len(best_tour) - 1))

    return best_tour, total_travel_cost, best_max_distance

# Execution and print tour details
tour, total_travel_cost, max_distance = find_bottleneck_tsp_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")