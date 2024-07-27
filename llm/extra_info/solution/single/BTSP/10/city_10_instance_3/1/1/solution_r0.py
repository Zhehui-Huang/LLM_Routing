import math
from itertools import permutations

# Destination coordinates
locations = [
    (84, 67),  # City 0: Depot
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Euclidean distance calculation
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate distance matrix
n = len(locations)
distance_matrix = [[euclidean_distance(locations[i], locations[j]) for j in range(n)] for i in range(n)]

# Function to evaluate a tour
def evaluate_tour(tour):
    total_cost = 0
    max_consecutive_distance = 0
    for i in range(1, len(tour)):
        dist = distance_matrix[tour[i-1]][tour[i]]
        total_cost += dist
        max_consecutive_distance = max(max_consecutive_distance, dist)
    return total_cost, max_consecutive_distance

# Generate all permutations excluding first city and find the minimum max_consecutive_distance
best_tour = None
best_total_cost = float('inf')
best_max_distance = float('inf')

for perm in permutations(range(1, n)):
    tour = [0] + list(perm) + [0]
    total_cost, max_dist = evaluate_tour(tour)
    if max_dist < best_max_distance or (max_dist == best_max_distance and total_cost < best_total_cost):
        best_tour, best_total_cost, best_max_distance = tour, total_cost, max_dist

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")