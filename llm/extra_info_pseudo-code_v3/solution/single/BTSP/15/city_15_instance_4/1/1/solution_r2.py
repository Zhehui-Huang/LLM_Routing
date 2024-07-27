import math
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Find all permutations of city visits, excluding the starting city 0
all_permutations = permutations(cities.keys() - {0})

# Iterating through each possible tour permutation
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

for perm in all_permutations:
    # Append the start city 0 at the beginning and end of the tour
    tour = (0,) + perm + (0,)
    # Calculate total cost and find the maximum distance between any two consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_line_distance(tour[i - 1], tour[i])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    # Compare with the best found so far
    if max_distance < best_max_distance:
        best_max_distance = max_distance
        best_tour = tour
        best_total_cost = total_cost

# Output the results
# The best tour, total travel cost and the maximum distance between any two consecutive cities
print(f"Tour: {list(best_torn)}")
print(f"Total travel cost: {best_total_cost}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")