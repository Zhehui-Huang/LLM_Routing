import math
from itertools import permutations

# Define city coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Get all permutations of cities except the depot city
city_permutations = permutations([i for i in range(1, len(cities))])

# Initialize variables to keep track of the best tour
best_tour = None
min_max_distance = float('inf')
best_total_cost = 0

# Evaluate each permutation
for perm in city_permutations:
    # Start and end at depot
    tour = [0] + list(perm) + [0]

    # Calculate the total return trip distance and max distance between consecutive cities
    total_cost = 0
    max_edge_cost = 0
    
    for i in range(len(tour) - 1):
        d = distance(tour[i], tour[i + 1])
        total_cost += d
        max_edge_cost = max(max_edge_cost, d)

    # Compare to the best found so far
    if max_edge_cost < min_max_distance:
        min_max_distance = max_edge_cost
        best_tour = tour
        best_total_cost = total_cost

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)
print("Maximum distance between consecutive cities:", min_max_distance)