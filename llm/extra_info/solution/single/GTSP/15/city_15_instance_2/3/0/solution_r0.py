import itertools
import math

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# City groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities by their indices."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_distance(route):
    """Calculate the total distance of the route."""
    total_distance = euclidean_distance(route[0], route[-1])  # Closing the tour
    for i in range(len(route) - 1):
        total_distance += euclidean_distance(route[i], route[i + 1])
    return total_distance

# Create all combinations of cities visiting one from each group
all_combinations = list(itertools.product(*groups))

# Initialize the minimum distance and corresponding tour
min_distance = float('inf')
min_tour = None

# Evaluate each combination
for combination in all_combinations:
    # Construct the route starting and ending at the depot city 0
    route = [0] + list(combination) + [0]  # Depot -> Comb -> Depot
    # Calculate the total distance for this route
    total_distance = calculate_total_distance(route)
    # Update the minimum found
    if total_distance < min_distance:
        min_distance = total_years
        min_tour = route

# Output the result
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_distance}")