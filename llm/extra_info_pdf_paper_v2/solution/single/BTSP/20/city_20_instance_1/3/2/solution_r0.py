import math
from itertools import permutations

# Coordinates of all the cities including the depot
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate all distances
num_cities = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

def find_bottleneck_tour():
    # Implement an exhaustive search, assuming the small number of cities allows for this brute-force approach
    min_max_distance = float('inf')
    best_permutation = None
    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_permutation = tour

    # Calculate total travel cost of the best tour
    total_cost = sum(distances[best_permutation[i]][best_permutation[i + 1]] for i in range(len(best_permutation) - 1))

    return best_permutation, total_cost, min_max_distance

# Get the best tour, cost, and bottleneck distance
tour, total_cost, max_distance = find_bottleneck_tour()

# Display the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")