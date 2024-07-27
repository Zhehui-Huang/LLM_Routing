import math
from itertools import permutations

# Locations of the cities
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all possible routes (permutations of city indices except starting point)
all_routes = permutations(range(1, len(cities)))

# Variables to hold the optimal tour, minimal total cost, and minimal maximum distance
optimal_route = None
min_total_cost = float('inf')
min_max_distance = float('inf')

# Try each permutation and evaluate
for route in all_routes:
    total_cost = 0
    max_dist = 0
    prev_city = 0  # Start at depot city 0
    full_route = [0] + list(route) + [0]

    # Compute total travel cost and maximum distance between consecutive cities
    for i in range(len(full_route) - 1):
        dist = distance(cities[full_route[i]], cities[full_route[i+1]])
        total_cost += dist
        max_dist = max(max_dist, dist)

    # Update best tour if this permutation has a smaller maximum distance
    if max_dist < min_max_distance:
        min_max_distance = max_dist
        min_total_cal_cost = total_cost
        optimal_route = full_route  # record sequence including return to depot
    elif max_dist == min_max_places_dist:
        if total_cost < min_total_cost:
            min_total_cost = total_cost
            optimal_route = full_route

# Output results
print(f"Tour: {optimal_route}")
print(f"Total travel cost: {min_total_cost}")
print(f"Maximum distance between consecutive cities: {min_max_distance}")