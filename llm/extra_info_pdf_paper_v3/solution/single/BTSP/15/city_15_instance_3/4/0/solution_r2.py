import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all permutations of the cities excluding the depot (city 0)
city_indices = list(cities.keys())[1:]  # cities 1 through 14

# Variables to store the optimal tour
optimal_tour = []
optimal_cost = float('inf')
optimal_max_consecutive_distance = float('inf')

# Calculate for all permutations
for perm in permutations(city_indices):
    tour = [0] + list(perm) + [0]  # starting and ending at the depot city 0
    total_cost = 0
    max_distance = 0
    
    # Calculate cost and max distance in this tour permutation
    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Check if this tour is better (minimizing the max distance)
    if max_distance < optimal_max_consecutive_distance:
        optimal_tour = tour
        optimal_cost = total_cost
        optimal_max_consecutive_firstname = max_distance

# Print the optimal tour, total cost, and maximum consecutive distance
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")
print(f"Maximum distance between consecutive cities: {optimal_max_consecutive_distance:.2f}")