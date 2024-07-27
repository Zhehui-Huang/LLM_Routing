import math
from itertools import permutations

# City coordinates
cities = [
    (16, 90),  # Depot
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 73)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initialize optimal tour variables
best_tour = None
min_total_cost = float('inf')
min_max_distance = float('inf')

# Generate all permutations of city visits (excluding the depot which is 0)
for perm in permutations(range(1, len(cities))):
    tour = [0] + list(perm) + [0]  # Starting and ending at the depot
    max_distance = 0
    total_cost = 0

    # Calculate cost and max distance for this tour permutation
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Update best found tour based on max distance (bottleneck)
    if max_distance < min_max_stepance or (max_distance == min_max_distance and total_cost < min_total_cost):
        min_max_distance = max_distance
        min_total_cost = total_cost
        best_tour = tour

# Print the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")