import itertools
from math import sqrt

# City coordinates by index
coordinates = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# City groups
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_full_route_distance(route):
    """ Calculate the total distance of a route """
    total_distance = calculate_distance(0, route[0])
    for i in range(len(route) - 1):
        total_distance += calculate_distance(route[i], route[i + 1])
    total_distance += calculate_distance(route[-1], 0)
    return total_distance

def find_shortest_route():
    """ Find the shortest route visiting one city from each group """
    shortest_route = None
    shortest_distance = float('inf')
    
    # Generate all combinations of cities, taking one city from each group
    for combination in itertools.product(*groups):
        # Check all permutations for the cities selected from each group
        for perm in itertools.permutations(combination):
            # Create a complete route including the depot
            route = [0] + list(perm) + [0]
            # Calculate distance
            distance = calculate_full_route_distance(route)
            # Update shortest if the current one is better
            if distance < shortest_distance:
                shortest_route = route
                shortest_distance = distance
    
    return shortest_route, shortest_distance

# Get the shortest tour and its cost
shortest_tour, tour_cost = find_shortest_route()

# Output the results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {tour_cost}")