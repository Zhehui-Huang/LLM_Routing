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
def euclidean_distance(a, b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the total distance of a given route
def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += euclidean_distance(route[i], route[i + 1])
    return total_distance

# Initialize variables for finding the best route and minimum distance
best_route = None
min_distance = float('inf')

# Generate all combinations of one city from each group
for combination in product(*city_groups):
    # Create a route starting and ending at the depot city, including one city from each group
    route = [0] + list(combination) + [0]
    # Calculate the distance of this route
    distance = calculate_total_distance(route)
    # If the calculated distance is less than the found minimum, update the best route and minimum distance
    if distance < min_distance:
        min_distance = distance
        best_route = route

# Output the results: the best route and the total travel cost
print(f"Tour: {best_route}")
print(f"Total travel cost: {min_distance:.2f}")