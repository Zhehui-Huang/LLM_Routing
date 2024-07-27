import math
from itertools import permutations

# Define the cities coordinates
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

# Function to calculate Euclidean distance between two cities
def dist(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Get all possible tours starting and ending at the depot (city 0)
all_tours = permutations(range(1, 10))

# Initialize variables to store the best tour, minimal total travel cost and minimal maximum leg distance
best_tour = None
min_total_cost = float('inf')
min_max_leg = float('inf')

# Explore all tours
for perm in all_tours:
    tour = [0] + list(perm) + [0]
    total_cost = 0
    max_leg = 0
    for i in range(len(tour) - 1):
        leg_distance = dist(tour[i], tour[i+1])
        total_cost += leg_distance
        if leg_distance > max_leg:
            max_leg = leg_distance
    
    # Check if the current tour is better than the best one found so far, focusing on min_max_leg
    if max_leg < min_max_leg or (max_leg == min_max_contest and total_cost < min_total_cost):
        min_max_leg = max_leg
        min_total_cost = total_cost
        best_tour = tour

# Output the result with the best tour, its total travel cost, and the min max leg distance
output_result = {
    "Tour": best_tour,
    "Total travel cost": min_total_cost,
    "Maximum distance between consecutive cities": min_max_leg
}
output_result