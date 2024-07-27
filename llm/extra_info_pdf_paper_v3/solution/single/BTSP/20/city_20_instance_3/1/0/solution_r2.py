import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}

# Function to calculate the Euclidean distance between two cities
def distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible permutations of city visits (excluding depot city 0)
permuted_paths = permutations(range(1, 20))

# Initialize variables for finding the best tour
best_path = None
min_max_distance = float('inf')
total_min_cost = float('inf')

# Trying every permutation of the cities
for path in permuted_paths:
    full_path = [0] + list(path) + [0]
    total_cost = 0
    max_distance = 0

    for i in range(len(full_path) - 1):
        d = distance(full_path[i], full_path[i + 1])
        total_cost += d
        if d > max_distance:
            max_distance = d
    
    # Update the best tour found based on minimization of maximum distance
    if max_distance < min_max_distance:
        best_path = full_path
        min_max_distance = max_distance
        total_min_cost = total_cost

# Output the best path, total travel cost, and maximum distance between two consecutive cities
print(f"Tour: {best_path}")
print(f"Total travel cost: {total_min_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")