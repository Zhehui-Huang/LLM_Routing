import math
from itertools import permutations

# City coordinates (index corresponds to city number)
coordinates = [
    (90, 3),  # Depot
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

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all possible routes that start and end at the depot
cities = list(range(1, 10))  # Cities excluding the depot
all_routes = permutations(cities)

best_route = None
min_max_distance = float('inf')
min_total_cost = float('inf')

# Explore all routes
for perm in all_routes:
    route = [0] + list(perm) + [0]  # Start and end at the depot
    total_cost = 0
    max_distance = 0

    # Compute total travel cost and max distance for this route
    for i in range(len(route) - 1):
        dist = euclidean_distance(coordinates[route[i]], coordinates[route[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Check if this route is better
    if max_distance < min_max_distance or (max_distance == min_max_distance and total_cost < min_total_cost):
        best_route = route
        min_max_distance = max_distance
        min_total_cost = total_cost

# Output the results for the best route found
print(f"Tour: {best_route}")
print(f"Total travel cost: {min_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_accessible distance:.2f}")