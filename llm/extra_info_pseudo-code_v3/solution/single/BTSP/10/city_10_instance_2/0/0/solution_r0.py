import math
from itertools import permutations

# Define the cities and their coordinates
coordinates = [
    (90, 3),   # Depot city 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Compute Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Get all the cities except the depot
cities = list(range(1, len(coordinates)))

# Find the best tour that minimizes the maximum distance between consecutive cities
best_tour = None
best_max_distance = float('inf')
best_total_cost = 0

# Explore all permutations of the cities
for perm in permutations(cities):
    # Include the depot at the start and end of the tour
    tour = [0] + list(perm) + [0]

    # Compute the total cost and the maximum distance in this tour
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Update the best tour if found a better one
    if max_distance < best_max_distance:
        best_tour = tour
        best_max_distance = max_distance
        best_total_cost = total_cost

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")