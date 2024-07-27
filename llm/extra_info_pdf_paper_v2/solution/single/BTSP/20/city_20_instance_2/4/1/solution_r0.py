import math
from itertools import permutations

# Coordinates of the cities including the depot city
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all permutations of city indices excluding the depot city (considering city 0 is the depot)
perm = permutations(range(1, len(cities)))

# Variables to keep track of the best solution found
min_bottleneck = float('inf')
best_tour = None

# Explore each permutation to find the optimal tour
for p in perm:
    route = [0] + list(p) + [0]  # Starting and ending at the depot city
    max_dist = max(distance(route[i], route[i+1]) for i in range(len(route) - 1))
    
    if max_dist < min_bottleneck:
        min_bottleneck = max_dist
        best_tour = route

# Calculate the total travel cost of the best tour
total_cost = sum(distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_bottleneck:.2f}")