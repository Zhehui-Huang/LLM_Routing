import math
from itertools import permutations

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generating all possible tours that start and end at the depot (city 0), visiting each city exactly once
all_tours = permutations([i for i in range(1, len(cities))])

# Variables to track the best tour and its stats
min_max_consecutive_distance = float('inf')
best_tour = None
best_total_cost = None

# Testing all possible permutations of the cities
for tour in all_tours:
    # Creating a full loop tour by adding the depot (starting and ending at city 0)
    full_tour = (0,) + tour + (0,)
    
    total_cost = 0
    max_consecutive_distance = 0
    
    # Calculate total tour cost and the max consecutive distance
    for i in range(len(full_tour) - 1):
        current_distance = distance(full_tour[i], full_tour[i + 1])
        total_cost += current_distance
        if current_distance > max_consecutive_distance:
            max_consecutive_distance = current_distance
            
    # Update the best tour if the current max consecutive distance is smaller
    if max_consecutive_distance < min_max_consecutive_distance:
        min_max_consecutive_distance = max_consecutive_distance
        best_tour = full_tour
        best_total_cost = total_cost

# Output the results
print("Tour:", list(best_tour))
print("Total travel cost:", best_total_cost)
print("Maximum distance between consecutive cities:", min_mk_consecutive_throwd, bothin_con_matching