import numpy as np
import random

# Defines the cities and their demands
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robot capacity
robot_capacity = 160
num_robots = 2

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate cost matrix
def do_cost_matrix(cities):
    n = len(cities)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            cost_matrix[i, j] = euclidean_distance(cities[i], cities[j])
    return cost_matrix

# Calculate cost savings
def do_cost_saving(cost_matrix):
    n = len(cost_matrix)
    savings = []
    depot_cost = cost_matrix[0]
    for i in range(1, n):
        for j in range(i + 1, n):
            savings.append(((i, j), depot_cost[i] + depot_cost[j] - cost_matrix[i][j]))
    return sorted(savings, key=lambda x: x[1], reverse=True)

def init_routes(cities):
    return [[0, i, 0] for i in range(1, len(cities))]

def is_feasible(route, demands, capacity):
    return sum(demands[city] for city in route if city != 0) <= capacity

# Implement route initialization using cost savings
def do_route(cost_savings, demands, capacity):
    routes = init_routes(cities)
    for ((i, j), saving) in cost_savings:
        if any(i in route for route in routes) and any(j in route for route in routes):
            route_i = next(route for route in routes if i in route)
            route_j = next(route for route in routes if j in route)
            if route_i != route_j:
                merged_route = route_i[:-1] + route_j[1:]
                if is_feasible(merged_route, demands, capacity):
                    routes.remove(route_i)
                    routes.remove(route_j)
                    routes.append(merged_route)
    return routes

def calculate_total_cost(routes, cost_matrix):
    total_cost = 0
    for route in routes:
        route_cost = sum(cost_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
        total_cost += route_cost
    return total_cost

# Cost matrix and savings calculation
cost_matrix = do_cost_matrix(cities)
cost_savings = do_cost_saving(cost_matrix)

# Initialize routes and find a plausible assignment for the given number of robots
routes = do_route(cost_savings, demands, robot_capacity)
assigned_routes = routes[:num_robots]

# Calculate cost for each route and total cost
total_costs = [calculate_total_cost([route], cost_matrix) for route in assigned_routes]
overall_total_cost = sum(total_costs)

# Output the results
for idx, route in enumerate(assigned_route):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {total_costs[idx]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")