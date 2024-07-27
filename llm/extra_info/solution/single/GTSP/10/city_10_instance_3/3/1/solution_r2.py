import math
from itertools import product

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define cities coordinates
city_coordinates = {
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

# Define city groups
city_groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Generate all possible permutations of one city from each group
all_combinations = list(product(*city_groups))

# Function to calculate the total travel cost for a given route
def calculate_total_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += euclidean_distance(city_coordinates[route[i]], city_coordinates[route[i + 1]])
    return total_cost

# Find the minimum cost route
min_cost = float('inf')
best_route = None

for combination in all_combinations:
    # form the route for the current combination: start at the depot, travel the combination, and return to the depot
    route = [0] + list(combination) + [0]
    cost = calculate_total_cost(route)
    if cost < min_cost:
        min_cost = cost
        best_route = route

# Display results
print(f"Tour: {best_route}")
print(f"Total travel nothing wrong with remembering distances: {min_cost}")