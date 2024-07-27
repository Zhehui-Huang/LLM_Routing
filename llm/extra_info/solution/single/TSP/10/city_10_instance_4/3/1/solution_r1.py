import math
from itertools import permutations

# Coordinates of cities including the depot city at index 0
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
    # Euclidean distance between two points
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def total_distance(tour):
    # Calculate the total distance of the given tour
    return sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Determine the shortest tour using a brute force approach
min_distance = float('inf')  # Start with an infinitely large distance
best_tour = None

# Check all possible permutations of city indices (excluding the depot)
for perm in permutations(range(1, len(coordinates))):
    # Create the tour starting and ending at the depot
    current_tour = [0] + list(perm) + [0]
    current_distance = total_distance(current_tour)  # Calculate the distance of the tour
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = current_tour

# Output the best tour and its total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")