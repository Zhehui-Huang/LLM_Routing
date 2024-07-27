import math
from itertools import permutations

# Define the coordinates of each city including the depot.
positions = [
    (8, 11),   # Depot City 0
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.hypot(positions[a][0] - positions[b][0], positions[a][1] - positions[b][1])

# Generate all possible tours starting and ending at the depot
def generate_tours():
    base_tour = list(range(1, len(positions)))  # City indices except the depot
    for perm in permutations(base_tour):
        yield [0] + list(perm) + [0]

# Evaluate the tours to find the one with the minimized maximum edge length
best_tour = None
min_max_distance = float('inf')
total_cost_of_best_tour = 0

for tour in generate_tours():
    max_distance_in_tour = 0
    total_cost_of_tour = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(tour[i], tour[i+1])
        total_cost_of_tour += distance
        if distance > max_distance_in_tour:
            max_distance_in_tour = distance
    if max_distance_in_tour < min_max_distance:
        best_tour = tour
        min_max_distance = max_distance_in_tour
        total_cost_of_best_tour = total_cost_of_tour

# Output the best found tour and associated costs
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost_of_best_tour:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")