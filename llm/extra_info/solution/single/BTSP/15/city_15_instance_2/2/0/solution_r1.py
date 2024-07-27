import math
from itertools import permutations

# Define city coordinates, depot is city index 0
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

# Compute the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Attempt to find the minimal longest distance in a tour that visits each city exactly once
best_tour = None
best_max_distance = float('inf')
best_total_cost = 0

# Iterate over all permutations of city indices excluding the depot (0)
for perm in permutations(range(1, 15)):
    tour = [0] + list(perm) + [0]
    max_distance = 0
    total_cost = 0

    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Check if the current permutation is better than what we found so far
    if max_distance < best_max_distance:
        best_max_distance = max_distance
        best_tour = tour
        best_total_cost = total_cost

# Output the final results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")