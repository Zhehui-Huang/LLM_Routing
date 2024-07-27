import math
from itertools import product

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Group of cities
city_groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2]
}


def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)


# Generate all possible city combinations adhering to the one city per group rule
combinations = list(product(*city_groups.values()))

min_distance = float('inf')
best_tour = []

# Evaluate each combination to find the shortest route
for combination in combinations:
    # Start at the depot, visit the combination of cities, and return to the depot
    tour = [0] + list(combination) + [0]
    total_distance = 0
    # Calculate the total tour distance
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i + 1])
    
    # Check if this tour is better than the previously found tours
    if total_distance < min_distance:
        min_distance = total_distance
        best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_distance)