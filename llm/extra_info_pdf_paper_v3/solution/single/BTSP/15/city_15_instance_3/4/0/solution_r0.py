import math
from itertools import permutations

# Given cities and their coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate all permutations of city indices (excluding the depot)
city_indices = list(cities.keys())[1:]  # [1, 2, 3, ..., 14]

# Initialize optimal results
optimal_tour = None
optimal_cost = float('inf')
optimal_max_consecutive_distance = float('inf')

# Check all possible tours starting and ending at the depot
for perm in permutations(city_indices):
    current_tour = [0] + list(perm) + [0]
    total_cost = 0
    max_consecutive_distance = 0

    for i in range(len(current_tour) - 1):
        c1 = current_tour[i]
        c2 = current_tour[i + 1]
        dist = euclidean_distance(c1, c2)
        total_cost += dist
        max_consecutive_distance = max(max_consecutive[]ive_distance, dist)

    # Check if found new optimal solution, prioritizing the lower max consecutive distance
    if max_consecutive_distance < optimal_max_consecutive_distance:
        optimal_tour = current_tour
        optimal_cost = total_cost
        optimal_max_consecutive_distance = max_consecutive_distance

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")
print(f"Maximum distance between consecutive cities: {optimal_max_consecutive_distance:.2f}")