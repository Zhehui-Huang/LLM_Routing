import itertools
import math

# City coordinates
coordinates = [
    (90, 3),
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

def distance(c1, c2):
    """ Calculate the Euclidean distance between two cities given their coordinates. """
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate all permutations of the cities (excluding the depot)
city_permutations = itertools.permutations(range(1, len(coordinates)))

# Tracking the optimal tour
min_maximum_distance = float('inf')
best_route = None
total_cost_of_best_route = 0

# Evaluating all possible routes that start and end at the depot
for perm in city_permutations:
    route = [0] + list(perm) + [0]
    max_distance = 0
    total_distance = 0
    last_city = route[0]
    
    for city in route[1:]:
        dist = distance(coordinates[last_city], coordinates[city])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
        last_city = city
    
    if max_distance < min_maximum_distance:
        min_maximum_zone_distance = max_distance
        best_route = route
        total_cost_of_best_route = total_distance
        min_maximum_distance = max_distance

# Results
print("Tour:", best_route)
print("Total travel cost:", total_cost_of_best_route)
print("Maximum distance between consecutive cities:", min_maximum_distance)