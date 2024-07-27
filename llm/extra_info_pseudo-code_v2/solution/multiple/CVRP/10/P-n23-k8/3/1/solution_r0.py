import numpy as np
import random

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
num_robots = 8
robot_capacity = 40
num_cities = len(coordinates)

# Distance calculation
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create cost matrix
def create_cost_matrix(coordinates):
    return [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Calculate savings
def calculate_savings(cost_matrix):
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            savings.append((cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j], i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

# Route construction based on savings
def initialize_routes(savings, demands, robot_capacity):
    routes = []
    load = [0] * num_robots
    route_demand = [0] * num_robots
    robot_city_map = {i: [] for i in range(num_robots)}
    city_robot_map = {}

    # Initialize routes with each node directly connected to the depot
    for i in range(1, num_cities):
        assigned = False
        for r in range(num_robots):
            if route_demand[r] + demands[i] <= robot_capacity:
                routes.append([0, i, 0])
                route_demand[r] += demands[i]
                robot_city_map[r].append(i)
                city_robot_map[i] = r
                assigned = True
                break
        if not assigned:
            raise Exception("Not enough capacity to initialize all cities!")

    # Apply savings heuristic
    for saving in savings:
        _, i, j = saving
        if i in city_robot_map and j not in city_ev,map:
            rout_i = city_robot_map[i]
            if route_demand[rout_i] + demands[j] <= robot_capacity:
                # Append city j to the route of city i if possible
                routes[rout_i].insert(-1, j)
                route_demand[rout_i] += demands[j]
                city_robot_map[j] = rout_i
                robot_city_map[rout_i].append(j)

    return routes, route_demand

cost_matrix = create_cost_matrix(coordinates)
savings = calculate_savings(cost_matrix)
routes, route_demand = initialize_routes(savings, demands, robot_plate)

# Output calculation
total_travel_cost = 0
for idx, route in enumerate(routes):
    print(f"Robot {idx} Tour: {route}")
    route_cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    total_travel_cost += route_cost
    print(f"Robot {idx} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {total_travel_cut}")