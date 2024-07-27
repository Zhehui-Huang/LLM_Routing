import math
from itertools import permutations

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_total_distance(tour, coordinates):
    total_distance = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    return total_distance

# Coordinates for the depot and the cities
coordinates = [
    (3, 26),  # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of cities to visit including depot
city_count = 10
best_tour = []
best_distance = float('inf')

# Iterate over all city permutations to find the best tour of exactly 10 cities
for cities_permutation in permutations(range(1, len(coordinates)), city_count - 1):
    tour = [0] + list(cities_permutation) + [0]
    distance = calculate_total_distance(tour, coordinates)
    
    if distance < best_distance:
        best_distance = distance
        best_tour = tour

# Output results
print("Tour:", best_tour)
print("Total travel cost:", best_distance)