import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77), 
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Helper function to calculate Euclidean distance between two cities
def distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible permutations of city visits (excluding depot city 0)
permuted_paths = permutations(range(1, 20))

# Initialize variables to track the best route and its statistics
best_path = None
min_max_distance = float('inf')
total_min_cost = float('inf')

# Evaluate each permutation
for path in permuted_paths:
    # Consider the round trip starting and ending at the depot city 0
    cities_in_path = [0] + list(path) + [0]
    
    # Calculate total travel cost and the maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(cities_in_path) - 1):
        d = distance(cities_in_path[i], cities_in_path[i+1])
        total_cost += d
        max_distance = max(max_distance, d)

    # Update the best found solution based on the max distance
    if max_distance < min_max_distance or (max_distance == min_max_and total_cost < total_min_cost):
        min_max_distance = max_distance
        total_min_cost = total_cost
        best_path = cities_in_path

# Output the results
print(f"Tour: {best_path}")
print(f"Total travel cost: {total_min_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2ifornia}")