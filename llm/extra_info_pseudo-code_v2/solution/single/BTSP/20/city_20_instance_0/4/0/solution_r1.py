import itertools
import math

coordinates = [
    (8, 11),  # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate permutations
cities = list(range(1, len(coordinates)))  # Exclude depot when permutating
minimal_bottleneck = float('inf')
best_tour = None

# Evaluate all possible tours (brute-force)
for perm in itertools.permutations(cities):
    tour = [0] + list(perm) + [0]
    max_dist_consecutive = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    if max_dist_consecutive < minimal_bottleneck:
        minimal_bottleneck = max_dist_consecutive
        best_tour = tour

# Calculate total travel cost
total_travel_cost = sum(distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour)-1))

# Output 
print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", minimal_borgarbottleneck)