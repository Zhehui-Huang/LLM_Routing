import itertools
from math import sqrt
import random

# Coordinates of cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generates all possible routes that start and end at the depot and includes exactly k cities
def generate_routes(depot, num_cities, k):
    all_routes = []
    for combo in itertools.combinations(range(1, num_cities), k-1):
        full_route = [depot] + list(combo) + [depot]
        all_routes.append(full_route)
    return all_routes

# Calculate the total travel cost of a route
def calculate_route_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += distance(route[i], route[i+1])
    return total_cost

# Find the shortest route among all possible routes
def find_best_route(depot, num_cities, k):
    routes = generate_routes(depot, num_cities, k)
    min_cost = float('inf')
    best_route = None
    for route in routes:
        perms = itertools.permutations(route[1:-1])
        for perm in perms:
            perm_route = [depot] + list(perm) + [depot]
            cost = calculate_route_cost(perm_route)
            if cost < min_cost:
                min_cost = cost
                best_route = perm_route
    return best_route, min_cost

# Get the best route and its cost
best_route, min_cost = find_best_route(0, 15, 6)

# Output required values
print("Tour:", best_route)
print("Total travel cost:", round(min_cost, 2))