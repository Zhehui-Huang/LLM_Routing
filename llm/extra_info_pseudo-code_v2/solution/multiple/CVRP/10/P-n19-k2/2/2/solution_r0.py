import numpy as np
from itertools import permutations
from math import sqrt
from copy import deepcopy

# City coordinates and demands
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Number of robots and their capacities
num_robots = 2
capacity = 160

# Euclidean distance function
def distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cost Matrix
cost_matrix = np.array([[distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))])

# Function to check capacity constraints
def valid_tour(tour, capacities, demands):
    load = 0
    for city in tour:
        load += demands[city]
        if load > capacities:
            return False
    return True

# Clarke-Wright Savings Algorithm
def clarke_wright():
    savings = []
    for i in range(1, len(cities)):
        for j in range(1, len(cities)):
            if i != j:
                s_ij = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
                savings.append((s_ij, i, j))
    # Sort savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])
    
    # Initialize routes
    routes = {i: [0, i, 0] for i in range(1, len(cities))}
    
    for _, i, j in savings:
        if valid_tour(routes[i] + [j], capacity, demands) and valid_tour(routes[j] + [i], capacity, demands):
            if routes[i][-2] == routes[j][1] and not set(routes[i][1:-1]).intersection(set(routes[j][1:-1])):
                # Merge routes
                new_route = routes[i][:-1] + routes[j][1:]
                if valid_tour(new_route, capacity, demands):
                    del routes[j]
                    routes[i] = new_route
    
    return routes

# Execute Clarke-Wright to get initial routes
routes = clarke_wright()
robots_routes = list(routes.values())[:num_robots]

# Calculate route costs
def calculate_cost(route):
    return sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

# Assign and output results
total_cost = 0
for i, route in enumerate(robots_routes):
    route_cost = calculate_cost(route)
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_cost}")
    total_cost += route_cost

print(f"Overall Total Travel SAVED: {total_cost}")