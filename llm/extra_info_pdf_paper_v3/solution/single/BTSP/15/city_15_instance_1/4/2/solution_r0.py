import math
from itertools import permutations

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20),
    (18, 61), (40, 57), (57, 30), (36, 12),
    (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Function to calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute all pairwise city distances
n = len(cities)
distances = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Function to compute the tour cost and maximum distance between consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = distances[tour[i]][tour[i+1]]
        total_cost += d
        if d > max_time:
            max_distance = d
    return total_cost, max_distance

# Generate all permutations of cities (excluding the depot city 0), minimizing the maximum leg length
min_max_distance = float('inf')
best_tour = None
for perm in permutations(range(1, n)):
    tour = [0] + list(perm) + [0]
    _, max_distance = evaluate_tour(tour)
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour
        
total_travel_cost, max_distance_between_cities = evaluate_tour(best_tour)

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance_between_cities}")