import math
import itertools
from random import shuffle, seed

seed(42)  # For reproducibility

# Define cities' coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73), 
    6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30), 
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible combinations of the cities that the robot can visit (excluding the depot city)
all_combinations = list(itertools.combinations(range(1, 15), 9))

# Find the combination with the minimal route length that includes returning to the depot
best_tour = None
min_distance = float('inf')

# Evaluate each combination of cities
for comb in all_combinations:
    # Include the depot in the tour
    full_tour = [0] + list(comb) + [0]
    
    # Compute all permutations of the selected cities to find the shortest path
    for perm in itertools.permutations(list(comb)):
        current_tour = [0] + list(perm) + [0]
        total_dist = sum(distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
        
        if total_dist < min_distance:
            min_distance = total_dist
            best_tour = current_tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_distance)