import math
from itertools import permutations

# Coordinates of Cities including the depot
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), 
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Groups of cities: each sublist represents a group from which exactly one city must be visited
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Function to calculate Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((coordinates[c1][0] - coordinates[c2][0]) ** 2 + (coordinates[c1][1] - coordinates[c2][1]) ** 2)

# Explore all combinations of choosing one city from each group (Cartesian product)
all_combinations = list(permutations([c[i] for i, c in enumerate(groups)]))

# Shortest tour initialization
shortest_tour = None
minimum_cost = float('inf')

# Evaluate each combination
for combination in all_combinations:
    # Starting at the depot
    current_tour = [0] + list(combination) + [0]
    current_cost = 0
    
    # Calculate the travel cost of this tour
    for i in range(len(current_tour) - 1):
        current_cost += distance(current_tour[i], current_tour[i + 1])
    
    # Check if this tour is the shortest found so far
    if current_cost < minimum_cost:
        shortest_tour = current_tour
        minimum_cost = current_cost

# Output the result
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {minimum_cost}")