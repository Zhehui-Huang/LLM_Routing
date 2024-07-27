import math
from itertools import permutations

# Coordinates for each city
coordinates = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
               (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Calculate Euclidean distance between two coordinates
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Prepare a matrix holding the distances between every pair of cities
n = len(coordinates)  # number of cities
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

# Function to evaluate a tour, returning the cumulative distance and the max leg distance
def evaluate_toueur(tour):
    max_distance = 0
    total_cost = 0
    for i in range(1, len(tour)):
        dist = distances[tour[i-1]][tour[i]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    # Include return to depot
    last_leg = distances[tour[-1]][tour[0]]
    total_cost += last_leg
    if last_leg > max_distance:
        max_distance = last_leg
    return max_distance, total_cost

# Check all permutations of cities (excluding the starting depot city)
for perm in permutations(range(1, n)):
    tour = [0] + list(perm) + [0]
    max_dist, total_cost = evaluate_toueur(tour)
    if max_dist < best_max_distance:
        best_max_distance = max_dist
        best_total_cost = total_cost
        best_tour = tour

# Outputting the best result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")