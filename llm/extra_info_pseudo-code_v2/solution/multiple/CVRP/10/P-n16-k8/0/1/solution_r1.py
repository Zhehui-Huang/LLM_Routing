import math
import numpy as np

# Data inputs for cities, demands, and robot capabilities
cities = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
])
demands = np.array([0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11])
num_robots = 8
robot_capacity = 35
depot = 0

# Compute Euclidean distance matrix
def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return dist_matrix

# Initialize robot routes
def initialize_routes(num_robots, depot):
    return {r: [depot] for r in range(num_robots)}

# Calculate route cost
def calculate_route_cost(route, dist_matrix):
    return sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

# Assign cities to robots in a way that respects capacity constraints
def assign_cities_to_robots(routes, demands, robot_capacity, dist_matrix):
    indices = list(range(1, len(demands)))
    demand_fulfilled = np.zeros(len(demands), dtype=bool)
    for r in routes:
        load = 0
        while load < robot_capacity and indices:
            for i in indices:
                if load + demands[i] <= robot_capacity and not demand_fulfilled[i]:
                    routes[r].append(i)
                    load += demands[i]
                    demand_fulfilled[i] = True
            if routes[r][-1] != depot:
                routes[r].append(depot)
            indices = [i for i in indices if not demand_fulfilled[i]]
    return routes

# Calculate total travel cost for all tours
def total_travel_cost(routes, dist_matrix):
    total = 0
    for r, route in routes.items():
        total += calculate_route_cost(route, dist_matrix)
    return total

# Running the solution
dist_matrix = calculate_distance_matrix(cities)
routes = initialize_routes(num_robots, depot)
routes = assign_cities_to_robots(routes, demands, robot_capacity, dist_matrix)
total_cost = total_travel_cost(routes, dist_matrix)

# Output results
print("Overall Total Travel Cost:", total_cost)
for robot_id, route in routes.items():
    route_cost = calculate_route_cost(route, dist_matrix)
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {route_cost}")