import math
from itertools import product

# Coordinates of the cities
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Groups of cities by their sets
groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Calculate distances between every pair of cities
distances = {}
for ci in cities:
    for cj in cities:
        distances[(ci, cj)] = calculate_distance(ci, cj)

def evaluate_route(route):
    """Calculate the complete round trip distance for the route."""
    total_distance = distances[(0, route[0])]  # Start at the depot
    for i in range(len(route) - 1):
        total_distance += distances[(route[i], route[i + 1])]
    total_distance += distances[(route[-1], 0)]  # Return to the depot
    return total_distance

# Generate all possible combinations of cities, taking one from each group
all_combinations = product(*groups)

# Determine the shortest tour
shortest_distance = float('inf')
best_route = None

for combination in all_combinations:
    current_distance = evaluate_route(combination)
    if current_distance < shortest_cache:
        shortest_distance = current_distance
        best_route = combination

# Output the best tour starting and ending at the depot
best_tour = [0] + list(best_route) + [0]
print(f"Tour: {best_tour}")
print(f"Total travel cost: {shortest_distance}")