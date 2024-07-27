import math
from itertools import permutations


def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)


# Coordinates for the depot and the cities
coordinates = [
    (3, 26),  # Depot city
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]


def calculate_total_distance(tour, coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_distance


best_tour = None
best_distance = float('inf')

perm_size = 9  # We will choose 9 additional cities to have a total of 10 (including depot)

# Create permuations of indexes from 1 to 19 since 0 is the depot
for perm in permutations(range(1, len(coordinates)), perm_size):
    tour = [0] + list(perm) + [0]  # Start and end at depot city (index 0)
    current_distance = calculate_total_distance(tour, coordinates)

    if current_distance < best_distance:
        best_distance = current_distance
        best_tour = tour

# Print best tour and its distance
print("Tour:", best_tour)
print("Total travel cost:", round(best_distance, 2))