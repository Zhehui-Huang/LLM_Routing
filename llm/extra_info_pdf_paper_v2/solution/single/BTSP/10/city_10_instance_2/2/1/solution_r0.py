import math
from itertools import permutations

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate all possible permutations of cities excluding the depot city
city_indices = list(range(1, len(cities)))
permutations_of_cities = permutations(city_indices)

# Initialize the best tour and distances
best_tour = None
minimal_bottleneck_distance = float('inf')
minimal_total_cost = float('inf')

# Check all permutations
for perm in permutations_of_cities:
    current_perm = [0] + list(perm) + [0]
    max_distance = 0
    total_cost = 0

    for i in range(len(current_perm) - 1):
        city_a = current_perm[i]
        city_b = current_perm[i + 1]
        dist = distance(cities[city_a], cities[city_b])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    if max_distance < minimal_bottleneck_distance:
        minimal_bottleneck_distance = max_distance
        best_tour = current_perm
        minimal_total_cost = total_cost

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", minimal_total_cost)
print("Maximum distance between consecutive cities:", minimal_bottleneck_distance)