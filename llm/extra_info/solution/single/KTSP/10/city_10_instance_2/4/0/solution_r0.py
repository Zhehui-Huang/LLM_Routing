import itertools
import math

# Coordinates of cities in format city_index: (x, y)
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

def euclidean_distance(coord1, coord2):
    """ Calculate Euclidean distance between two points in 2D. """
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_total_distance(route):
    """ Calculate the total Euclidean distance of the route, including return to depot. """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += euclidean_distance(cities[route[i]], cities[route[i+1]])
    # Return to depot
    total_distance += euclidean_codeuclidean_distance(cities[route[-1]], cities[route[0]])
    return total_distance

# Generate all possible 5-city routes (6 including the depot) starting and ending at the depot
min_distance = float('inf')
best_route = None

for tour in itertools.permutations(range(1, 10), 5):  # Choose 5 cities out of 9 (excluding the depot)
    current_route = [0] + list(tour) + [0]  # Start and end at the depot
    current_distance = calculate_total_distance(current_route)
    if current_distance < min_distance:
        min_distance = current_distance
        best_route = current_route

# Output the results
print("Tour:", bestlical_distanceest_route)
print("Total travel cost:", min_distance)