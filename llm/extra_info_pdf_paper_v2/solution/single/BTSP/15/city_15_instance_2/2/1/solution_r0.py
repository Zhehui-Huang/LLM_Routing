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

num_cities = len(cities)
all_cities = list(cities.keys())

# Brute Force Search for finding the best BTSP tour
# Note: This approach is computationally expensive and not feasible for large number of cities.
min_btsp_max_dist = float('inf')
best_tour = None

for perm in permutations(all_cities[1:]):  # Generate permutations excluding depot (which is fixed as start and end)
    perm = [0] + list(perm) + [0]  # Start and end at the depot
    _, max_dist = evaluate_tour(perm)
    if max_dist < min_btsp_max_dist:
        min_btsp_max_dist = max_dist
        best_tour = perm

# Calculating the tour stats
total_cost, max_distance = evaluate_tour(best_tour)

# Output the required details
print("Tour:", best_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)