import itertools
import math

# Coordinates of cities
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
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_total_distance(route):
    """ Calculate the total travel cost of a route. """
    total_distance = 0
    # Sum distances for all adjacent pairs in the tour
    for i in range(len(route) - 1):
        total_distance += euclidean_distance(cities[route[i]], cities[route[i+1]])
    # Add distance back to the depot
    total_distance += euclidean_distance(cities[route[-1]], cities[route[0]])
    return total_distance

# Store minimum distance found and corresponding route
min_distance = float('inf')
best_route = None

# Permutations of 5 cities from the 9 (excluding the depot)
for tour in itertools.permutations(range(1, 10), 5):
    current_route = [0] + list(tour) + [0]  # Route starts and ends at the depot
    current_distance = calculate_total_distance(current_route)
    if current_distance < min_distance:
        min_distance = current_distance
        best_route = current_route

# Print the best tour and its total travel cost
print("Tour:", best_route)
print("Total travel travel_distance:", min_distance)