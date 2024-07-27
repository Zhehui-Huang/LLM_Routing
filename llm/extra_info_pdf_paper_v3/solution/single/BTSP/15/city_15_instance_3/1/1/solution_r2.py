import math
from itertools import permutations

# Coordinates for each city
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73),
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30),
    (70, 95), (29, 64), (32, 79)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize distance matrix
n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define variables for tracking the best tour found
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

# Function to evaluate a tour, returning the cumulative distance and the max leg distance
def evaluate_tour(tour):
    max_distance = 0
    total_cost = 0
    for i in range(1, len(tour)):
        dist = distances[tour[i-1]][tour[i]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist  # Track the maximum distance between consecutive cities
    return_to_depot = distances[tour[-1]][tour[0]]
    total_cost += return_to_depot
    if return_to_depot > max_distance:
        max_distance = return_to_depot
    return max_distance, total_cost

# Iterate over permutations of city indices (excluding the depot)
for perm in permutations(range(1, n)):
    tour = [0] + list(perm) + [0]  # Construct a tour starting and ending at the depot
    max_dist, total_cost = evaluate_tour(tour)
    if max_dist < best_max_distance:
        best_max_distance = max_dist
        best_total_cost = total_cost
        best_tour = tour

# Output the best tour found
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")