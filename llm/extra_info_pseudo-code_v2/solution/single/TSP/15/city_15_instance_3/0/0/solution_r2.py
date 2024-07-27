import math
from itertools import permutations

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour, coordinates):
    """Calculate the total distance of the tour based on the coordinates."""
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

def two_opt(tour, coordinates):
    """Apply 2-opt algorithm to find a short tour."""
    min_change = True
    while min_change:
        min_change = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                old_distance = euclidean_distance(coordinates[tour[i]], coordinates[tour[i - 1]]) + euclidean_distance(coordinates[tour[j]], coordinates[tour[j - 1]])
                new_distance = euclidean_distance(coordinates[tour[i]], coordinates[tour[j - 1]]) + euclidean_distance(coordinates[tour[i - 1]], coordinates[tour[j]])
                if new_distance < old_distance:
                    tour[i:j] = reversed(tour[i:j])
                    min_change = True
    return tour

# Define coordinates of the cities, including the depot (city 0)
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Initialize a naive tour that goes through each city once and returns to the depot
initial_tour = list(range(len(coordinates))) + [0]

# Optimize the tour using the 2-opt algorithm
optimized_tour = two_opt(initial_tour, coordinates)

# Calculate the total cost of the optimized tour
optimized_cost = total_distance(optimized_tour, coordinates)

# Output the results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {optimized_cost:.2f}")