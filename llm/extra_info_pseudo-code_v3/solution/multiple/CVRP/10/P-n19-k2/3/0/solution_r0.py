import numpy as np
from itertools import permutations
from math import sqrt

# Setting up city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands per city (excluding the depot)
demands = [
    0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15
]

# Total robots and their capacity
num_robots = 2
capacity = 160

# Function to calculate Euclidean distance
def distance(city1, city2):
    return sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Creating distance matrix
n = len(coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = distance(coordinates[i], coordinates[j])

# Constructing an initial valid solution
def initial_solution():
    # Greedy approach: init solution starts from the depot and picks next nearest city that fits capacity
    unvisited = set(range(1, n))  # Exclude depot at first
    routes = []
    for _ in range(num_robots):
        route = [0]  # start at depot
        load = 0
        while unvisited:
            next_city = None
            min_dist = float('inf')
            current_city = route[-1]
            for city in unvisited:
                if load + demands[city] <= capacity and distance_matrix[current_city][city] < min_dist:
                    next_city = city
                    min_dist = distance_matrix[current_city][city]
            if next_city is None:
                break
            route.append(next_city)
            load += demands[next_city]
            unvisited.remove(next_city)
        if route[-1] != 0:
            route.append(0)  # return to depot
        routes.append(route)
    return routes

# Calculate total travel cost for the routes
def calculate_costs(routes):
    total_cost = 0
    details = []
    for route in routes:
        cost = 0
        for i in range(len(route) - 1):
            cost += distance_matrix[route[i]][route[i+1]]
        details.append((route, cost))
        total_cost += cost
    return total_cost, details

# Generating init solution and calculating costs
routes = initial_solution()
total_cost, route_details = calculate_costs(routes)

# Display the results
for idx, details in enumerate(route_details):
    print(f'Robot {idx} Tour: {details[0]}')
    print(f'Robot {idx} Total Travel Cost: {details[1]:.2f}')
print(f'Overall Total Travel Cost: {total_cost:.2f}')