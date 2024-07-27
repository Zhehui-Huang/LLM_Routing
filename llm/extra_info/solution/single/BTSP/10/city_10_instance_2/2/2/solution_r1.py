import math
import itertools

# Define the cities with their coordinates
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all permutations of the cities excluding the depot (0)
city_indices = list(range(1, len(cities)))
all_routes = itertools.permutations(city_indices)

best_route = None
min_max_distance = float('inf')
total_cost_of_best_route = 0

# Evaluate each possible route
for route in all_routes:
    route_with_depot = [0] + list(route) + [0]
    max_distance = 0
    total_cost = 0
    for i in range(len(route_with_depot) - 1):
        d = distance(route_with_depot[i], route_with_depot[i + 1])
        total_cost += d
        max_distance = max(max_distance, d)
    
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_route = route_with_depot
        total_cost_of_best_route = total_cost

# Output the optimized tour results
print(f"Tour: {best_route}")
print(f"Total travel cost: {total_cost_of_best_route:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")