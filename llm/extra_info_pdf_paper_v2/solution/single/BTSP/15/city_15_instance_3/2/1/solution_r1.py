import math
from itertools import permutations

# Coordinates of the cities
coordinates = [
    (16, 90),  # City 0 (depot)
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

num_cities = len(coordinates)

# Compute Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Evaluate the tour to find total distance and maximum leg distance
def evaluate_tour(tour):
    total_distance = 0
    max_leg_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(tour[i], tour[i+1])
        total_distance += dist
        max_leg_distance = max(max_leg_distance, dist)
    return total_distance, max_leg_distance

# Generate all possible tours starting and ending at the depot, assessing each
best_tour = None
best_total_distance = float('inf')
best_max_leg_distance = float('inf')

for perm in permutations(range(1, num_cities)):
    tour = [0] + list(perm) + [0]
    total_distance, max_leg_distance = evaluate_tour(tour)
    if max_leg_distance < best_max_leg_distance:
        best_tour = tour
        best_total_distance = total_distance
        best_max_leg_distance = max_leg_distance

print("Tour:", best_tour)
print("Total travel cost:", best_total_distance)
print("Maximum distance between consecutive cities:", best_max_leg_distance)