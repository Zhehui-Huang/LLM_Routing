import itertools
import math

# Coordinates of the depot and each city
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Groups of cities
groups = [
    [1, 2, 5, 6], 
    [8, 9, 10, 13], 
    [3, 4, 7], 
    [11, 12, 14]
]

# Function to calculate Euclidean distance between two points
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible combinations of cities, taking one city from each group
all_possible_routes = itertools.product(*groups)

# Find the shortest route
min_distance = float('inf')
best_route = None

for route in all_possible_routes:
    # Always start and end at depot city 0
    full_route = [0] + list(route) + [0]
    total_distance = 0
    
    # Calculate the total travel distance of the full route
    for i in range(len(full_border) - 1):
        total_distance += calculate_distance(full_border[i], full_border[i + 1])
    
    if total_distance < min_distance:
        min_distance = total_distance
        best_route = full_border

# Output the solution
print("Tour:", best_route)
print("Total travel cost:", min_distance)