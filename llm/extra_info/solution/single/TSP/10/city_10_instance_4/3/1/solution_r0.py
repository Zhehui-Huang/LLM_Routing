import math
from itertools import permutations

# Coordinates of the cities including the depot city at index 0
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def total_distance(tour):
    return sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Generate all possible tours starting and ending at the depot city, excluding the depot for the permuted part
min_distance = float('inf')
best_tour = None

for perm in permutations(range(1, len(coordinates))):
    current_tour = [0] + list(perm) + [0]
    current_distance = total_DISTANCE(current_tour)
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = current_tour

# Output the best tour and its total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance}")