import numpy as np
import random
import math

# Given data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]
num_robots = 8
num_cities = len(coordinates)

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Creating a distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Assign cities to robots (simple initial division)
cities_per_robot = num_cities // num_robots

# Initial routes: naive split of consecutive cities
routes = [[i for i in range(j * cities_per_robot, (j + 1) * cities_per_robot)] for j in range(num_robots)]
for i in range(num_cities % num_robots):
    routes[i].append(num_robots * cities_per_robot + i)

# Simulated Annealing (SA) parameters
T = 10000 # initial temperature
T_min = 1  # minimum temperature
alpha = 0.99  # cooling rate

def calculate_cost(route):
    cost = distance_matrix[0][route[0]]  # Starting from depot city 0
    for k in range(len(route) - 1):
        cost += distance_matrix[route[k]][route[k + 1]]
    return cost

def simulated_annealing(route):
    temp = T
    current_route = route.copy()
    current_cost = calculate_cost(current_route)
    while temp > T_min:
        # Randomly swap two cities in the route
        i, j = sorted(random.sample(range(len(route)), 2))
        new_route = current_route[:]
        new_route[i], new_route[j] = new_route[j], new_route[i]
        new_cost = calculate_cost(new_route)
        cost_change = new_cost - current_cost
        # Accept new route if it improves cost or probabilistically if it increases cost
        if cost_change < 0 or random.random() < math.exp(-cost_change / temp):
            current_route = new_route
            current_cost = new_cost
        temp *= alpha
    return current_route, current_cost

optimized_routes = []
total_cost = 0

for route in routes:
    optimal_route, route_cost = simulated_annealing(route)
    # Add the return to the depot city 0 (although it's not necessary after visit)
    optimal_route.append(0)
    optimized_routes.append(optimal_route)
    total_cost += route_cost
    print(f"Robot Tour: {optimal_route}")
    print(f"Robot Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {total_cost}")