import math
from itertools import permutations

# Coordinates of each city including the depot
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
    13: (72,43),
    14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Evaluate a given tour: computes total cost and maximum distance between consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Generating all permutations of the cities excluding the depot, and manually adding the start/end at the depot.
min_max_dist = float('inf')
optimal_tour = None
optimal_total_cost = 0

for perm in permutations(list(cities.keys())[1:]):  # cities except the depot
    tour = [0] + list(perm) + [0]
    total_cost, max_dist = evaluate_tour(tour)
    if max_dist < min_max_dist:
        min_max_dist = max_dist
        optimal_tour = tour
        optimal_total_cost = total_cost

# Print the optimal tour found, its total travel cost, and the max distance between consecutive cities
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_total_cost, 2))
print("Maximum distance between consecutive cities:", round(min_max_dist, 2))