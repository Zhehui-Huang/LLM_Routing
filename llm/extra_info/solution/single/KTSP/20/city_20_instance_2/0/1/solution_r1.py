import math
from itertools import permutations

# Coordinates for the depot and the cities
coordinates = [
    (3, 26),  # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_distance(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Configuration for search
city_count = 10  # Including the depot
best_tour = None
best_distance = float('inf')

# Generate permutations of 9 cities (excluding the depot which is 0 and is a fixed start/end)
for perm in permutations(range(1, len(coordinates)), city_count - 1):
    current_tour = [0] + list(perm) + [0]  # Start and end at the depot
    current_distance = calculate_total_distance(current_tour, coordinates)
    
    if current_distance < best_distance:
        best_distance = current_distance
        best_tour = current_tour

# Output the best tour found and its travel cost
print("Tour:", best_tour)
print("Total travel cost:", round(best_distance, 3))