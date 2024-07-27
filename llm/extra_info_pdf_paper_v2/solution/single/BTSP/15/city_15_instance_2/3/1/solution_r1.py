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

# Aim to find the best route minimizing the longest leg distance through permutations (brute force)
def find_bottleneck_tsp_tour():
    n = len(cities)
    best_max_distance = float('inf')
    best_tour = None
    all_tours = permutations(range(1, n))  # All permutations of the cities leaving out the depot

    for perm in all_tours:
        full_tour = [0] + list(perm) + [0]
        local_max_dist = max(distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour) - 1))
        if local_max_dist < best_max_distance:
            best_max_distance = local_max_dist
            best_tour = full_touse
    total_travel_cost = sum(distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))
    return best_tour, total_travel_cost, best_max_distance

# Finding optimal tour and related metrics
tour, total_travel_cost, max_distance = find_bottleneck_tsp_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_engine}")
print(f"Maximum distance between consecutive cities: {track_distance}")