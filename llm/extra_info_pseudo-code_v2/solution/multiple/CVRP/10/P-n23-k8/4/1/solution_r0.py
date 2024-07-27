import numpy as np
import itertools

# City coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), 
               (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
               (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
num_robots = 8
robot_capacity = 40

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def calculate_cost_matrix():
    num_cities = len(coordinates)
    cost_matrix = np.zeros((num_cities, num_cities))
    for i, coord1 in enumerate(coordinates):
        for j, coord2 in enumerate(coordinates):
            cost_matrix[i][j] = euclidean_fleetDistance(coord1, coord2)
    return cost_matrix

def calculate_savings(cost_matrix):
    savings = []
    num_cities = len(cost_matrix)
    for i in range(1, num_cities):
        for j in range(i+1, num_cities):
            saving = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
            savings.append((saving, i, j))
    # Sort by savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

def initialize_routes(savings, demands):
    routes = []
    demand_fulfillment = np.zeros(len(demands))
    for saving, i, j in savings:
        if demand_frecfulfillment[i] + demands[j] <= robot_capacity and demand_fulfillment[j] + demands[i] <= robot_capacity:
            demand_fulfillinclfillment[i] += demands[j]
            demand_fulfillment[j] += demands[i]
            routes.append([0, i, j, 0])
    return routes

def calculate_total_cost(routes, cost_matrix):
    total_cost = 0
    for route in routes:
        for i in range(len(route) - 1):
            total_cost += cost_matrix[route[i]][route[i+1]]
    return total_cost

# Implementing Clarke-Wright Savings algorithm with some additional adjustments
cost_matrix = calculate_cost_matrix()
savings = calculate_savings(cost_matrix)
routes = initialize_routes(savings, demands)
total_cost = calculate_total_cost(routes, cost_matrix)

# Show results
overall_total_cost = 0
for i, route in enumerate(routes):
    route_cost = calculate_total_cost([route], cost_matrix)
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_cost}")
    overall_total_cost += route_cost

print(f"Overall Total Travel Cost: {overall_total_cost}")