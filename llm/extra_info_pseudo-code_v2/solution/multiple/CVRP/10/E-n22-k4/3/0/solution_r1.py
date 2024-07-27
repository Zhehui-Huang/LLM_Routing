import math
import numpy as np
from collections import defaultdict

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Parameters
number_of_robots = 4
robot_capacity = 6000
depot_index = 0

def calculate_distance_matrix(coords):
    num_cities = len(coords)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)
    return matrix

def savings_list(distance_matrix):
    num_cities = len(distance_matrix)
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            savings.append((i, j, distance_matrix[depot_index][i] + distance_matrix[depot_index][j] - distance_matrix[i][j]))
    return sorted(savings, key=lambda x: x[2], reverse=True)

def clarke_wright_algorithm(distance_matrix, demands, capacity):
    num_cities = len(distance_matrix)
    routes = []
    available = set(range(1, num_cities))
    route_demand = defaultdict(int)

    # Clarke-Wright Savings
    sl = savings_list(distance_matrix)

    while available:
        for i, j, saving in sl:
            if i in available and j in available:
                if route_demand[i] + demands[j] <= capacity and route_demand[j] + demands[i] <= capacity:
                    route_demand[i] += demands[j]
                    route_demand[j] += demands[i]
                    routes.append([depot_index, i, j, depot_index])
                    available.remove(i)
                    available.remove(j)
                    break

    # Cover all cities, if some are still not included, create direct routes
    for city in available:
        if demands[city] <= capacity:
            routes.append([depot_index, city, depot_index])
            available.remove(city)

    return routes

def calculate_route_costs(routes, distance_matrix):
    total_cost = 0
    costs = []
    for route in routes:
        cost = 0
        for i in range(len(route) - 1):
            cost += distance_matrix[route[i]][route[i+1]]
        costs.append(cost)
        total_cost += cost
    return costs, total_cost

# Calculate distance matrix
dist_matrix = calculate_distance_matrix(coordinates)

# Generate routes
routes = clarke_wright_algorithm(dist_matrix, demands, robot_capacity)

# Calculate costs
route_costs, overall_total_cost = calculate_route_costs(routes, dist_matrix)

# Output the results
for idx, route in enumerate(routes):
    print(f"Robot {idx % number_of_robots} Tour: {route}")
    print(f"Robot {idx % number_of_robots} Total Travel Cost: {route_costs[idx]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")