import math
from random import choice, shuffle
from copy import deepcopy

# ----------------------------------------------------------
# STEP 1: Initialize the Problem
# ----------------------------------------------------------

# City Coordinates and Demands
cities = {
    0: (30, 40, 0),
    1: (37, 52, 7),
    2: (49, 49, 30),
    3: (52, 64, 16),
    4: (31, 62, 23),
    5: (52, 33, 11),
    6: (42, 41, 19),
    7: (52, 41, 15),
    8: (57, 58, 28),
    9: (62, 42, 8),
    10: (42, 57, 8),
    11: (27, 68, 7),
    12: (43, 67, 14),
    13: (58, 48, 6),
    14: (58, 27, 19),
    15: (37, 69, 11),
    16: (38, 46, 12),
    17: (61, 33, 26),
    18: (62, 63, 17),
    19: (63, 69, 6),
    20: (45, 35, 15)
}

# Robots information
num_robots = 2
robot_capacity = 160

# ----------------------------------------------------------
# STEP 2: Calculate Distance Matrix
# ----------------------------------------------------------

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
n = len(cities)
dist_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# ----------------------------------------------------------
# STEP 3: Construct Initial Solution
# ----------------------------------------------------------

def find_minimal_route(start, cities, demands, capacities):
    route = [start]
    current_load = 0
    current = start
    
    while len(route) < len(cities):
        next_city = None
        min_dist = float('inf')
        
        for city in cities:
            if city not in route and current_load + demands[city] <= capacities and dist_matrix[current][city] < min_dist:
                min_dist = dist_matrix[current][city]
                next_city = city
        if next_city is None:
            break
        
        route.append(next_city)
        current_load += demands[next_city]
        current = next_city

    route.append(start) # return to depot
    return route

def create_initial_solution():
    unserved_cities = list(range(1, n))
    shuffle(unserved_cities)
    routes = []
    loads = []
    
    for _ in range(num_robots):
        if not unserved_cities:
            break
        current_route = find_minimal_route(0, unserved_cities, lambda i: cities[i][2], robot_capacity)
        routes.append(current_route)
        load = sum(cities[city][2] for city in current_route if city != 0)
        loads.append(load)
        unserved_cities = [city for city in unserved_cities if city not in current_route]
    
    return routes, loads

routes, loads = create_initial_solution()

# ----------------------------------------------------------
# STEP 4: Output the Solution
# ----------------------------------------------------------

def calculate_route_cost(route, dist_matrix):
    cost = 0
    for i in range(1, len(route)):
        cost += dist_matrix[route[i-1]][route[i]]
    return cost

total_cost = 0
for i, route in enumerate(routes):
    route_cost = calculate_route_cost(route, dist_matrix)
    total_cost += route_cost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {round(route_cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")