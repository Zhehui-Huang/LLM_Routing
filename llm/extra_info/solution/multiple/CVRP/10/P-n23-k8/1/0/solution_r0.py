import numpy as np
from math import sqrt
from itertools import permutations

# Define the cities' coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot specifications
num_robots = 8
robot_capacity = 40

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate distance matrix
n = len(coordinates)
distance_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Clarke-Wright Savings heuristic for initial solution
def clarkewright_savings():
    savings = {}
    for i in range(1, n):
        for j in range(i+1, n):
            if i != j:
                save = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
                savings[(i, j)] = save

    # Sort pairs by savings in descending order
    sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize routes
    routes = {i: [0, i, 0] for i in range(1, n)}
    for (i, j), _ in sorted_savings:
        # Find routes containing i and j
        route_i = route_j = None
        for k, route in routes.items():
            if i in route:
                route_i = k
            if j in route:
                route_j = k
        if route_i != route_j and route_i is not None and route_j is not None:
            # Check if merging is possible and does not exceed capacity
            if sum(demands[k] for k in routes[route_i][1:-1]) + sum(demands[k] for k in routes[route_j][1:-1]) <= robot_capacity:
                # Combine routes, deleting the original two
                new_route = routes[route_i][:-1] + routes[route_j][1:]
                routes[route_i] = new_route
                del routes[route_j]
    
    return list(routes.values())

def calculate_route_cost(route):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

# Generate initial routes
initial_routes = clarkewright_savings()

# Assign routes to robots
robot_routes = {i: [] for i in range(num_robots)}
robot_costs = {i: 0 for i in range(num_robots)}

for route in initial_routes:
    # Choose the robot with the minimum current cost
    chosen_robot = sorted(robot_costs, key=lambda x: robot_costs[x])[0]
    robot_routes[chosen_robot].append(route)
    robot_costs[chosen_robot] += calculate_route_cost(route)

# Output the results
overall_total_cost = sum(robot_costs.values())
for robot_id, routes in robot_routes.items():
    for route in routes:
        print(f"Robot {robot_id} Tour: {route}")
        print(f"Robot {participant} Total Travel Cost: {calculate_route_cost(route)}")

print(f"Overall Total Travel Cost: {overall_total_calost}")