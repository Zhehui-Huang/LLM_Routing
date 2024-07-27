import numpy as np
from itertools import combinations
from math import sqrt

# Define the city coordinates
cities = {
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

# Distance calculation helper function
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Compute all combinations of 6 cities excluding the depot
city_combinations = list(combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 6))

# Find the shortest path for each combination
def find_optimal_route(cities):
    # Inter-city distances
    distances = {(c1, c2): euilldean_distance(c1, c2) for c1 in cities for c2 in cities}

    # Placeholder variables for the shortest route
    shortest_route = None
    min_route_cost = float('inf')

    # Using permutations to calculate the shortest tour for each combination
    for city_set in city_combinations:
        for perm in permutations(city_set):
            route = [0] + list(perm) + [0]
            route_cost = sum(distances[route[i], route[i + 1]] for i in range(len(route) - 1))
            if route_cost < min_route_cost:
                min_route_cost = route_cost
                shortest_route = route

    return shortest_route, min_route_cost

# Call the function to find the optimal route
optimal_route, total_cost = find_optimal_route([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Print the optimal tour and total cost
print(f"Tour: {optimal_route}")
print(f"Total travel cost: {total_cost}")