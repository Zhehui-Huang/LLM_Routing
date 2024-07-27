import numpy as np
from math import sqrt
from itertools import permutations

# Define the cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Define the demand at each city
demand = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Vehicles Information
number_of_robots = 2
capacity = [160, 160]

# Calculate the Euclidean distance matrix
def calculate_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Heuristic solution construction
def greedy_solution():
    # List of all cities except the depot to be visited
    cities_to_visit = list(range(1, len(coordinates)))
    # Initialize routes
    routes = [[] for _ in range(number_of_robots)]
    # Capacity remaining in each robot
    remaining_capacity = capacity.copy()
    # Start and end at the depot
    for i in range(number_of_robots):
        routes[i].append(0)

    for city in cities_to_visit:
        # Attach cities to the nearest possible route if capacity allows
        assigned = False
        for i in range(number_of_robots):
            if remaining_capacity[i] >= demand[city]:
                routes[i].append(city)
                remaining_capacity[i] -= demand[city]
                assigned = True
                break
        if not assigned:
            # If no fitting route is found, return an error
            print("It is not possible to satisfy demand within the capacity constraints.")
            return
        
    # Closing each route by returning to the depot.
    for i in range(number_of_robots):
        routes[i].append(0)

    return routes

# Calculate total cost of the tours
def calculate_route_cost(routes):
    total_cost = 0
    costs = []
    for route in routes:
        route_cost = 0
        for i in range(len(route) - 1):
            route_cost += distance_matrix[route[i]][route[i + 1]]
        costs.append(route_cost)
        total_cost += route_cost
    return costs, total_cost

# Get the initial routes
initial_routes = greedy_solution()
route_costs, overall_cost = calculate_route_cost(initial_routes)

# Display the results
for idx, route in enumerate(initial_desc_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_costs[idx]:.2f}")

print(f"Overall Total Travel Salesman Travel Cost: {overall_cost:.2f}")