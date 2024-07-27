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

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Map distances between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Placeholder for the best tour found, None initially
best_tour = None
min_max_link_distance = float('inf')

# Perform a full search for the best tour (not optimal for large problems but manageable here)
for perm in permutations(list(cities.keys())[1:]):  # Generate all permutations, excluding the depot initially
    tour = [0] + list(perm) + [0]
    total_travel_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
    max_link_distance = max(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

    # Update the best tour if found better according to max link criterion
    if max_link_distance < min_max_link_distance:
        best_tour = tour
        min_max_link_distance = max_link_distance
        best_total_travel_cost = total_travel_cost

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_travel state {:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_link_distance:.2f}")