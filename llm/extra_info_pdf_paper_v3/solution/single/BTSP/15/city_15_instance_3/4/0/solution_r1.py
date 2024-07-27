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
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate city permutations excluding the depot, which is city 0
city_indices = list(cities.keys())[1:]  # From city 1 to city 14

# Initialize variables to find the optimal solution
optimal_tour = None
optimal_cost = float('inf')
optimal_max_consecutive_distance = float('inf')

# Explore each permutation representing a potential tour
for perm in permutations(city_indices):
    current_tour = [0] + list(perm) + [0]  # Always start and end at the depot
    total_cost = 0
    max_consecutive_distance = 0
    
    # Calculate total travel cost and max consecutive distance for this permutation
    for i in range(len(current_tour) - 1):
        c1 = current_tour[i]
        c2 = current_tour[i + 1]
        dist = euclidean_distance(c1, c2)
        total_cost += dist
        if dist > max_consecutive_distance:
            max_consecutive_distance = dist
    
    # Update when a better (lower maximum consecutive distance) tour is found
    if max_consecutive_distance < optimal_max_consecutive_distance:
        optimal_tour = current_tour
        optimal_cost = total_cost
        optimal_max_consecutive_distance = max_consecutive_distance

# Output the optimal solutions found
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")
print(f"Maximum distance between consecutive cities: {optimal_max_consecutive_distance:.2f}")