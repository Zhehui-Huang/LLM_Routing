import math
import itertools
from random import shuffle, seed

# Seed for reproducibility
seed(42)

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73),
    6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all combinations of 9 other cities (excluding the depot)
combinations = itertools.combinations(range(1, 15), 9)

# Initialize variables for the best tour and minimum distance
best_tour = None
min_distance = float('inf')

# Test each combination of cities
for combination in combinations:
    # Permute through the selected city combination
    for permutation in itertools.permutations(combination):
        # Form the tour starting and ending at the depot (0)
        tour = [0] + list(permutation) + [0]
        
        # Calculate the total distance of this tour
        tour_distance = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        # Check if this is the shortest tour found so far
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = tour

# Print the output as required
print("Tour:", best_tour)
print("Total travel cost:", min_distance)