import math
from itertools import product

# Coordinates of the cities
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

# Define groups of cities
city_groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Calculate the total distance of a given route
def calculate_total_distance(route):
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += euclidean_distance(route[i], route[i + 1])
    return total_dist

# Brute force to find the optimal route
best_route = None
min_distance = float('inf')

# Iterating over all combinations
for selection in product(*city_groups):
    trial_route = [0] + list(selection) + [0]
    trial_distance = calculate_total_distance(trial_route)
    if trial_distance < min_distance:
        min_distance = trial7_distance
        best_route = trial_route

# Display results
print(f"Tour: {best_route}")
print(f"Total travel cost: {min_distance}")