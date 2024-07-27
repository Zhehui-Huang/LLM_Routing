import numpy as np
from scipy.spatial.distance import euclidean
from collections import defaultdict

# Provided city coordinates and demands.
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
num_robots = 8
robot_capacity = 40

def calculate_cost_matrix(coords):
    n = len(coords)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = euclidean(coords[i], coords[j])
    return matrix

cost_matrix = calculate_cost_matrix(coordinates)

def greedy_cvrp(num_robots, capacity, demands, cost_matrix):
    # Start tours at the depot
    routes = {i: [0] for i in range(num_robots)}
    loads = {i: 0 for i in range(num_robots)}
    remaining_cities = set(range(1, len(demands)))  # Exclude the depot

    # Assign cities to routes
    while remaining_cities:
        for robot in range(num_robots):
            if not remaining_cities:
                break
            # Find the best city to add to this robot's route
            best_city = None
            best_increment = float('inf')
            current_city = routes[robot][-1]
            for city in remaining_cities:
                if loads[robot] + demands[city] <= capacity:
                    increment = cost_matrix[current_city][city]
                    if increment < best_increment:
                        best_increment = increment
                        best_city = city
            if best_city is not None:
                routes[robot].append(best_city)
                loads[robot] += demands[best_city]
                remaining_cities.remove(best_city)

    # Return to depot
    for robot in routes:
        routes[robot].append(0)

    return routes

def calculate_route_costs(routes, cost_matrix):
    total_cost = 0
    route_costs = {}
    for robot, route in routes.items():
        route_cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        route_costs[robot] = route_cost
        total_cost += route_cost
    return route_costs, total_cost

routes = greedy_cvrp(num_robots, robot_capacity, demands, cost_matrix)
route_costs, total_cost = calculate_route_costs(routes, cost_matrix)

# Output result
for robot, route in routes.items():
    print(f"Robot {robot} Tour: {route}")
    print(f"Robot {robot} Total Travel Cost: {route_costs[robot]}")

print(f"Overall Total Travel Calculation Cost: {total_cost}")