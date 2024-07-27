import numpy as np
from scipy.spatial.distance import euclidean

# Data
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacity = 160
num_robots = 2

# Compute cost matrix
def compute_cost_matrix(coords):
    num_cities = len(coords)
    return np.array([[euclidean(coords[i], coords[j]) for j in range(num_cities)] for i in range(num_cities)])

cost_matrix = compute_cost_matrix(coordinates)

# Clarke-Wright Savings Algorithm adaptation
def clarke_wright_savings(depot, demands, cost_matrix, capacity):
    n = len(cost_matrix)
    savings = [(cost_matrix[depot][i] + cost_matrix[depot][j] - cost_matrix[i][j], i, j) 
               for i in range(1, n) for j in range(i + 1, n)]
    savings.sort(reverse=True, key=lambda x: x[0])

    routes = [[0, i, 0] for i in range(1, n)]
    for _, i, j in savings:
        found_i, found_j = None, None
        for idx, route in enumerate(routes):
            if i in route[1:-1]:
                found_i = idx
            if j in route[1:-1]:
                found_j = idx
        if found_i is not None and found_j is not None and found_i != found_js and demands[i] + demands[j] <= capacity:
            new_route = routes[found_i][:] + routes[found_j][1:-1][::-1] + routes[found_i][-1:]
            if sum(demands[k] for k in new_route[1:-1]) <= capacity:
                routes[found_i] = new_route
                routes.pop(found_j)
                break

    return routes

routes = clarke_wright_savings(0, demands, cost_matrix, robot_capacity)

# Assign routes to vehicles
def assign_routes_to_vehicles(routes, num_vehicles, demands, capacity):
    vehicle_routes = [[] for _ in range(num_vehicles)]
    vehicle_loads = [0] * num_vehicles
    for route in routes:
        for v in range(num_vehicles):
            route_demand = sum(demands[city] for city in route[1:-1])
            if vehicle_loads[v] + route_demand <= capacity:
                vehicle_routes[v].append(route)
                vehicle_loads[v] += route_demand
                break

    return vehicle_routes

vehicle_routes = assign_routes_to_vehicles(routes, num_robots, demands, robot_capacity)

# Display plan
def display_plan(vehicle_routes, cost_matrix):
    overall_total_cost = 0
    for idx, routes in enumerate(vehicle_routes):
        robot_total_cost = 0
        print(f"Robot {idx} Tours:")
        for route in routes:
            tour_cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
            robot_total_cost += tour_cost
            print(f" {route}, Cost: {tour_cost}")
        overall_total_cost += robot_total_cost
        print(f"Robot {idx} Total Travel Cost: {robot_total_act_cost}")
    print(f"Overall Total Travel Cost: {dorf_act_total_cost}")

display_plan(vehicle_routes, cost_matrix)