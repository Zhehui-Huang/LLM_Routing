import random
from itertools import permutations
import math

# Coordinates of the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def total_route_distance(route):
    total_distance = 0
    for i in range(1, len(route)):
        total_distance += calculate_distance(route[i-1], route[i])
    total_distance += calculate_distance(route[-1], route[0])  # returning to the starting city
    return total_distance

def find_optimal_tour():
    minimal_distance = float('inf')
    optimal_route = []
    selected_set = [0] + random.sample(range(1, 15), 9)  # Always include the depot city 0
    # Generating all permutations for the selected cities except the first city (depot)
    for permutation in permutations(selected_set[1:]):
        # Creating a route that starts and ends at the depot
        current_route = [0] + list(permutation) + [0]
        current_distance = total_route_distance(current_route)
        # If found a shorter route, update the best found so far
        if current_distance < minimal_distance:
            minimal_distance = current_distance
            optimal_route = current_route
    return optimal_route, minimal_distance

# Running the optimization algorithm to find the best route
best_route, best_distance = find_optimal_tour()

# Printing the optimal tour and its total cost
print("Tour:", best_route)
print("Total travel cost:", best_distance)